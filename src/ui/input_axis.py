##################################################################################
# An input that is controlled by two keys and can have 3 values, -1, 0, 1
#
# Example: in a FPS game, keys W and S control forward and backward movement
#
#   pressing W,        output is +1 or move forward
#   pressing S,        output is -1 or move backward
#   pressing nothing,  output is 0 or don't move
###################################################################################

from src.ui.input_base import Input


class Axis(Input):

    def __init__(self, action_name, pygame_key_pair_list):
        self.value = 0
        self.action_name = action_name
        self.pygame_key_pair_list = pygame_key_pair_list

    def set_value(self, events):
        pass

    def get_value(self):
        pass
