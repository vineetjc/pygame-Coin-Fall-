##########################################################
# game manager
# will have global game variables like score and settings
##########################################################


class Game_Manager(object):
    def __init__(self, animation_manager):
        self.score = 0
        self.time = 0
        self.params = None
        self.animation_manager = animation_manager

    def set_input(self, input):
        self.input = input

    def set_highscore(self, highscore_manager):
        self.highscore_manager = highscore_manager

    def set_ai(self, ai_manager):
        self.ai_manager = ai_manager

    def reset(self):
        self.score = 0
        self.time = 0
