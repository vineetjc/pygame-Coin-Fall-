from src.misc.game_enums import Game_Mode


class Screen(object):
    def __init__(self, pygame, res, surface, size):
        self.pygame = pygame
        self.res = res
        self.surface = surface
        self.size = size
        self.images = {}
        self.texts = {}
        self.buttons = {}
        self.center_x = size[0] / 2
        self.center_y = size[1] / 2

    def update(self, events):
        return Game_Mode.MAIN_MENU
