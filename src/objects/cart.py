##################
# Cart Class
##################
import math
from src.misc.game_enums import Entity


class Cart(object):
    def __init__(self, res, size, surface, game_manager):
        self.type = Entity.CART
        self.res = res
        self.size = size
        self.surface = surface
        self.game_manager = game_manager
        self.input = game_manager.input
        self.animation_manager = game_manager.animation_manager
        self.image = res.cart_img
        self.x = (size[0] / 2) - 80
        self.y = size[1] - 120
        self.points = 0  # Changed Points to points
        self.dead = False  # Add this for game end check
        self.speed = 10

    def move(self):
        movement = self.input.get_axis('horizontal') * self.speed
        desired_movement = self.x + movement
        final_movement = max(min(desired_movement, self.size[0] - 140), -10)
        self.x = final_movement

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

    def collect_item(self, coin):
        if 645 > coin.y > 633:
            if ((self.x < coin.x + (55.0 / 2) < self.x + 160) and
                    (self.x < coin.x) and (self.x + 160 > coin.x + 55)):
                try:
                    if not coin.collected:
                        if coin.type == Entity.BLUE_COIN:
                            self.points += 3 * self.game_manager.difficulty.value["SCORE_MULTIPLIER"]
                        elif coin.type == Entity.BOMB:
                            self.dead = True  # Replace quit with death
                        else:
                            self.points += 1 * self.game_manager.difficulty.value["SCORE_MULTIPLIER"]

                        coin.collect()
                        if coin.type is Entity.COIN:
                            self.animation_manager.create_new_effect(
                                self.res.blast_anim2, self.res.blast_anim2_size, 0, False, (coin.x, coin.y))
                        elif coin.type is Entity.BLUE_COIN:
                            self.animation_manager.create_new_effect(
                                self.res.blast_anim3, self.res.blast_anim3_size, 0, False, (coin.x, coin.y))

                except AttributeError:
                    pass
