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

<<<<<<< HEAD:src/input_package/input_button.py
    def __init__(self, action_name, pygame_key_list):
        self.value = False
        self.action_name = action_name
        self.pygame_key_list = pygame_key_list

    def set_value(self, key_state):
        for key in self.pygame_key_list:
            if key_state[key]:
                self.value = 1
                return
=======
	def __init__(self, action_name, pygame_key_list):
		self.value = 0
		self.action_name = action_name
		self.pygame_key_list = pygame_key_list

	def set_value(self, events):
		pass

	def get_value(self):
		pass
>>>>>>> master:src/ui/input_button.py
