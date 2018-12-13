##########################################################
# game manager
# will have global game variables like score and settings
##########################################################

from src.misc.game_enums import Difficulty


class Game_manager(object):
    def __init__(self):
        self.score = 0
        self.time = 0
        self.difficulty = Difficulty.MEDIUM

    def reset(self):
        self.score = 0
        self.time = 0
	
	
        
