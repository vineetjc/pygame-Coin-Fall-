################
# Coin class
################
import random
from src.misc.game_enums import Entity
from src.animation_package import Animation


class Coin():
    def __init__(self, res, size, surface):
        self.type = Entity.COIN
        self.surface = surface
        self.animation = Animation(
            None, surface, res.silver_coin_anim, res.silver_coin_anim_size, 3, True)
        self.x = random.randint(50, size[0] - 50)
        self.y = -50
        self.anim_index = 0
        self.anim_counter = 0
        self.anim_tick_length = 4
        self.collected = False

    def fall(self):
        self.y += 7  # Change the value if necessary

    def draw(self):
        if self.collected:
            return

        self.animation.draw((self.x, self.y))

    def advance_animation(self):
        self.anim_counter += 1

        if self.anim_counter > self.anim_tick_length:
            self.anim_counter = 0
            self.anim_index += 1

            if self.anim_index >= len(self.images):
                self.anim_index = 0

    def collect(self):
        self.collected = True
