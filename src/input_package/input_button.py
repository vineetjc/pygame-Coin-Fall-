#################################################
# An input that is controlled by a keypress
# Example: in a FPS game, key R to reload
# Buttons can be mapped to multiple keys
# Example: Reload can be done by key R or key E
# or a key on the joystick
#################################################

from .input_base import Input
import pygame.key


class Button(Input):

    def __init__(self, action_name, pygame_key_list):
        self.value = 0
        self.action_name = action_name
        self.pygame_key_list = pygame_key_list

    def set_value(self, event):
        if event.key not in self.pygame_key_list:
            return
        else:
            if event.type == pygame.KEYUP:
                self.value += -1
                if self.value > 1: self.value = 1
            else
                self.value += 1
                if self.value < 0: self.value = 0

    def get_value(self):
        pass
