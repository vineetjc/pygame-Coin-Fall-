import sys
import pygame
from pygame.locals import QUIT, KEYUP
from src.misc.game_enums import Game_mode, Entity
from src.managers import *
from src.game_screens.screens_manager import Screen_Manager
from src.input_package import input_manager


def game_loop():
    pygame.init()
    res = Resources(pygame)

    # setup the window display
    size = (1024, 768)
    windowSurface = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption('Coin Fall')
    pygame.display.set_icon(res.logo)

    # initialize game variables
    game_clock = pygame.time.Clock()
    game_mode = Game_mode.MAIN_MENU
    game_manager = Game_manager()
    game_manager.set_input(input_manager.Input_Manager())
    screen_manager = Screen_Manager(pygame, res, windowSurface, size, game_clock, game_manager)

    while True:
        events = pygame.event.get()
        game_manager.input.update(events)
        game_mode = screen_manager.show(game_mode, events)
        game_clock.tick(60)


if __name__ == "__main__":
    game_loop()
