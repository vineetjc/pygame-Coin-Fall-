##################################
# Cart Class for AI mode
##################################
import math
import pygame
from src.misc.game_enums import Entity
from .cart import Cart


class Cart_AI(Cart):
    def __init__(self, res, size, surface, game_manager, image):
        Cart.__init__(self, res, size, surface, game_manager)
        self.image = image

    def move(self, ai_input=0):
        if ai_input < 0:
            ai_input = -1

        if ai_input > 0:
            ai_input = 1

        movement = ai_input * self.speed
        desired_movement = self.x + movement
        final_movement = max(min(desired_movement, self.size[0] - 140), -10)
        self.x = final_movement
