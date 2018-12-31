import sys
import pygame
from pygame.locals import QUIT, KEYUP, DOUBLEBUF, HWSURFACE
from src.misc.game_enums import Game_Mode, Entity
from src.managers import *
from src.game_screens.screens_manager import Screens_Manager
from src.input_package.input_manager import Input_Manager
from src.managers.highscore_manager import Highscore_Manager
from src.ai_package.ai_manager import AI_Manager
from src.animation_package import *


def game_loop():
    pygame.init()
    size = (1024, 768)
    windowSurface = pygame.display.set_mode(
        size, pygame.DOUBLEBUF | pygame.HWSURFACE)
    pygame.display.set_caption('Coin Fall')
    pygame.mouse.set_visible(True)
    res = Resources(pygame, size)
    pygame.display.set_icon(res.logo)
    game_clock = pygame.time.Clock()
    game_mode = Game_Mode.MAIN_MENU
    animation_manager = Animation_Manager(windowSurface)
    game_manager = Game_Manager(animation_manager)
    game_manager.set_input(Input_Manager())
    game_manager.set_highscore(Highscore_Manager())
    game_manager.set_ai(AI_Manager())
    screens_manager = Screens_Manager(
        pygame, res, windowSurface, size, game_clock, game_manager)
    sound_manager = Sound_Manager('background_music')
    sound_manager.play_background_music()

    while True:
        events = pygame.event.get()
        game_manager.input.update(events)
        game_mode = screens_manager.show(game_mode, events)
        pygame.display.flip()
        game_clock.tick(60)


if __name__ == "__main__":
    game_loop()
