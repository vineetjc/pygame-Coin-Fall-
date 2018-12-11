##########################################################
# game manager
# will have global game variables like score and settings
##########################################################


class Game_manager(object):

    def __init__(self):
        self.score = 0
        self.time = 0

    def set_input(self, input):
        self.input = input

    def reset(self):
        self.score = 0
        self.time = 0
