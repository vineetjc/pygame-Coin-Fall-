################
# Coin class
################
import random


class Coin():
    def __init__(self, res, size):
        self.image = res.coin_img
        self.images = res.silver_coin_images
        self.x = random.randint(0, size[0] - 55)
        self.y = -15

    def fall(self):
        self.y += 7  # Change the value if necessary

    def draw(self, surface):
        try:
            if len(self.images) == 0:
                surface.blit(self.image, (self.x, self.y))
            else:
                surface.blit(self.images[0], (self.x, self.y))
        except AttributeError:
            pass
