from src.misc.game_enums import Game_mode

class Screen(object):
    def __init__(self, pygame, res, surface):
        self.pygame = pygame
        self.res = res
        self.surface = surface
        self.buttons = {}

    def update(self, events):
        return Game_mode.MAIN_MENU
