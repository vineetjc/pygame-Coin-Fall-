import pygame
import sys
import random
import math

from pygame.locals import QUIT, KEYUP

from src.resources import Resources
from src.game_enums import Game_mode, Entity

from src.cart import Cart
from src.coin import Coin
from src.bluecoin import BlueCoin
from src.bomb import Bomb

from src.main_menu_screen import Main_menu_screen
from src.game_screen import Game_screen
from src.settings_screen import Settings_screen
from src.game_over_screen import Game_over_screen
from src.tutorial_screen import Tutorial_screen


def game_loop():
    pygame.init()

    # setup the window display
    size = (1024, 768)
    windowSurface = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption('Super Mumbo Epicness')

    # initialize resources and game mode
    res = Resources(pygame)
    game_clock = pygame.time.Clock()
    game_mode = Game_mode.MAIN_MENU

    # initialize screens
    main_menu_screen = Main_menu_screen(pygame, res, windowSurface)
    game_screen = Game_screen(pygame, res, windowSurface, size, game_clock)
    settings_screen = Settings_screen(pygame, res, windowSurface)
    game_over_screen = Game_over_screen(pygame, res, windowSurface)
    tutorial_screen = Tutorial_screen(pygame, res, windowSurface)

    # game loop starts
    while True:
        events = pygame.event.get()

        if game_mode == Game_mode.MAIN_MENU:
            game_mode = main_menu_screen.update(events)

        elif game_mode == Game_mode.GAME:
            game_mode = game_screen.update(events)

        elif game_mode == Game_mode.SETTINGS:
            game_mode = settings_screen.update(events)

        elif game_mode == Game_mode.GAME_OVER:
            game_mode = game_over_screen.update(events)

        elif game_mode == Game_mode.TUTORIAL:
            game_mode = tutorial_screen.update(events)

        else:
            pygame.quit()
            sys.exit()

        game_clock.tick(60)


if __name__ == "__main__":
    game_loop()
