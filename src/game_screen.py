from src.screen import Screen
from src.game_enums import Game_mode


class Game_screen(Screen):
    def __init__(self, pygame, res, surface):
        Screen.__init__(self, pygame, res, surface)
        pass

    def update(self, events):
        
        return Game_mode.GAME
