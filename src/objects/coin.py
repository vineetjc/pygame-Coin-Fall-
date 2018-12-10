################
# Coin class
################
import random
from src.misc.game_enums import Entity


class Coin():
    def __init__(self, res, size, surface):
        self.type = Entity.COIN
        self.surface = surface
        self.image = res.coin_img
        self.images = res.silver_coin_images
        self.x = random.randint(0, size[0] - 55)
        self.y = -15
        self.anim_index = 0
        self.anim_counter = 0
        self.anim_tick_length = 4
        self.collected = False

    def fall(self):
        self.y += 7  # Change the value if necessary

    def draw(self):
        if self.collected:
            return

        try:
            if len(self.images) == 0:
                self.surface.blit(self.image, (self.x, self.y))
            else:
                self.surface.blit(self.images[self.anim_index], (self.x, self.y))
                self.advance_animation()
        except AttributeError:
            pass

    def advance_animation(self):
        self.anim_counter += 1

        if self.anim_counter > self.anim_tick_length:
            self.anim_counter = 0
            self.anim_index += 1

            if self.anim_index >= len(self.images):
                self.anim_index = 0

    def collect(self):
        self.collected = True

