import pygame
import sys
import random
import math

from pygame.locals import QUIT, KEYUP

from src.managers.resources import Resources
from src.misc.game_enums import Game_mode, Entity
from src.managers.game_manager import Game_manager
from src.managers.input_manager import Input_Manager

from src.objects.cart import Cart
from src.objects.coin import Coin
from src.objects.bluecoin import BlueCoin
from src.objects.bomb import Bomb

from src.game_screens.main_menu_screen import Main_menu_screen
from src.game_screens.game_screen import Game_screen
from src.game_screens.settings_screen import Settings_screen
from src.game_screens.game_over_screen import Game_over_screen
from src.game_screens.tutorial_screen import Tutorial_screen
from src.game_screens.credits_screen import Credits_screen


def game_loop():
    pygame.init()

    # setup the window display
    size = (1024, 768)
    windowSurface = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption('Coin Fall')

    # initialize resources and game mode
    res = Resources(pygame)
    game_clock = pygame.time.Clock()
    game_mode = Game_mode.MAIN_MENU
    game_manager = Game_manager()
    input_manager = Input_Manager()

    # set game logo
    pygame.display.set_icon(res.logo)
    
    # initialize screens
    main_menu_screen = Main_menu_screen(pygame, res, windowSurface)
    game_screen = Game_screen(pygame, res, windowSurface, size, game_clock, game_manager)
    settings_screen = Settings_screen(pygame, res, windowSurface)
    game_over_screen = Game_over_screen(pygame, res, windowSurface, game_manager)
    tutorial_screen = Tutorial_screen(pygame, res, windowSurface)
    credits_screen = Credits_screen(pygame, res, windowSurface)
    

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

        elif game_mode == Game_mode.CREDITS:
            game_mode = credits_screen.update(events)

        else:
            pygame.quit()
            sys.exit()

        game_clock.tick(60)


if __name__ == "__main__":
    game_loop()
