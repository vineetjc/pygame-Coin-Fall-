#################################################
# An input that is controlled by a keypress
# Example: in a FPS game, key R to reload
# Buttons can be mapped to multiple keys
# Example: Reload can be done by key R or key E
# or a key on the joystick
#################################################

from src.ui.input_base import Input


class Button(Input):

    def __init__(self, action_name, pygame_key_list):
        self.value = 0
        self.action_name = action_name
        self.pygame_key_list = pygame_key_list

    def set_value(self, events):
        pass

    def get_value(self):
        pass
