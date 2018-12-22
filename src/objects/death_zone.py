##############################################
# Death zone at the bottom of the screeen
# Any coins reaching here will be destroyed
##############################################
from pygame import Rect


class Death_Zone:

    def __init__(self, size):
        temp_rect = Rect((0, 0), size)
        temp_rect.topleft = (0, size[1] + 50)
        self.collision_rect = temp_rect

    def check_collision(self, coin):
        return self.collision_rect.colliderect(coin.collision_rect())
