# AI Package User Guide
This package helps you in creating an AI for the Coin Fall game. How to create and test your own AI and some examples are explained in this guide. 
Main features
- Easy to create AI
- Easy to integrate with the game

# How to use

### Create a new AI script
Create a new AI class, make AI_Base as it's base class. Preferably create this class in a separate file in the ai_package folder.
A very simple AI example with explanation of all the functions in AI_Base clas s-
```python
import random
from .ai_base import AI_Base


class AI_New(AI_Base):

    #Called at the start of the game
    def __init__(self):
        pass
    
    # Called when game restarts
    def restart(self):
        pass

    # Called every frame
    # param: entity_list - a list containing all the entities: silver coins, gold coins and bombs on the screen
    # param: cart - reference to the cart object in the game
    # return: value - return either -1, 0 or 1.
    #               1 will move the cart right, -1 will move it left and 0 will stop it
    def update(self, entity_list, cart):
        random_movement = random.random(0, 1) * 2 - 1
        return random_movement

    # Called at the end of game, when either time expires or a bomb explodes
    def game_over(self):
        pass
```
This AI will move the cart randomly every frame.

### How to use your AI script in the game
It's very simple to use your AI in the game and will require just 2 changes in the ai_manager.py file and select AI mode in the game - 
```python
# Import your new AI class
from .ai_new import AI_New


class AI_Manager():

    def __init__(self):
        # self.ai is the currently active AI script and will be used by the game to send updates and get AI input
        # Initialize you AI script here
        self.ai = AI_Avoid_Bomb()

```

# Examples
### AI based on Perlin Noise
AI which uses Perlin Noise to create a better random AI
```python
from .ai_base import AI_Base
from src.simplex_noise_package.noise import PerlinNoise, normalize


class AI_Simplex(AI_Base):

    def __init__(self):
        self.pn = PerlinNoise(num_octaves=7, persistence=0.1)
        self.noise_index = 0

    def restart(self):
        self.noise_index = 0

    def update(self, entity_list, cart):
        self.noise_index += 1
        
        # This gives a value which moves near 0.0 in a less random manner
        random_movement = normalize(self.pn.noise(self.noise_index)) * 2 - 1

        # Don't move if the deviation is very small from zero
        if abs(random_movement) < 0.02:
            random_movement = 0
        
        # You can return float values, but it will be converted to either -1, 0 or 1
        return random_movement
```

### AI which actively avoids Bombs
AI which uses bomb's position relative to the cart's position to actively avoid it.
```python
import math
from .ai_base import AI_Base
from src.misc.game_enums import Entity


class AI_Avoid_Bomb(AI_Base):

    def __init__(self):
        pass

    def restart(self):
        pass

    def update(self, entity_list, cart):
        cart_x = cart.get_center()[0]
        entity_list_copy = entity_list.copy()
        
        # Get a list of bombs that are above the cart
        bombs_list = [x for x in entity_list_copy if (x.type is Entity.BOMB) and (x.y < 600)]

        if len(bombs_list) > 0:
        
            # Only using the lowest bomb for decision making
            lowest_bomb_x = bombs_list[0].x
        else:
            lowest_bomb_x = cart_x

        delta = lowest_bomb_x - cart_x

        # If we are safely away from the bomb, no need to move, else move away from bomb
        if abs(delta) > 150:
            ai_movement = 0
        else:
            if delta > 0:
                ai_movement = -1
            else:
                ai_movement = 1

        if len(bombs_list) == 0:
            ai_movement = 0

        return ai_movement

```
