##########################################################
# game manager
# will have global game variables like score and settings
##########################################################

from src.misc.game_enums import Difficulty


class Game_manager(object):
    def __init__(self, animation_manager):
        self.score = 0
        self.time = 0
        self.difficulty = Difficulty.MEDIUM
        self.animation_manager = animation_manager

    def set_input(self, input):
        self.input = input

    def reset(self):
        self.score = 0
        self.time = 0
