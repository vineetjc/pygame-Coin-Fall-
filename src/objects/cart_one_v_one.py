##################################
# Cart Class for one v one mode
##################################
import math
import pygame
from src.misc.game_enums import Entity
from .cart import Cart


class Cart_One_V_One(Cart):
    def __init__(self, res, size, surface, game_manager, image, axis_name, offset_x):
        Cart.__init__(self, res, size, surface, game_manager)
        self.image = image
        self.axis_name = axis_name
        self.x += offset_x

    def move(self):
        movement = self.input.get_axis(self.axis_name) * self.speed
        desired_movement = self.x + movement
        final_movement = max(min(desired_movement, self.size[0] - 140), -10)
        self.x = final_movement
