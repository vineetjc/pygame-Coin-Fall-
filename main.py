import sys
import pygame
from pygame.locals import QUIT, KEYUP
from src.misc.game_enums import Game_mode, Entity
from src.managers import *
from src.game_screens.screens_manager import Screens_Manager
from src.input_package.input_manager import Input_Manager
from src.animation_package import *


def game_loop():
    pygame.init()
    size = (1024, 768)
    windowSurface = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption('Coin Fall')
    res = Resources(pygame)
    pygame.display.set_icon(res.logo)
    game_clock = pygame.time.Clock()
    game_mode = Game_mode.MAIN_MENU
    animation_manager = Animation_Manager(windowSurface)
    game_manager = Game_manager(animation_manager)
    game_manager.set_input(Input_Manager())
    screens_manager = Screens_Manager(
        pygame, res, windowSurface, size, game_clock, game_manager)
    play_music = Play_sound('background_music')
    play_music.play_background_music()

    while True:
        events = pygame.event.get()
        game_manager.input.update(events)
        game_mode = screens_manager.show(game_mode, events)
        game_clock.tick(60)


if __name__ == "__main__":
    game_loop()
