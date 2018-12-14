import sys
import pygame
from pygame.locals import QUIT, KEYUP
from src.misc.game_enums import Game_mode, Entity
from src.managers import *
from src.game_screens import *
from src.input_package import input_manager

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
	game_manager.set_input(input_manager.Input_Manager())

	# set game logo
	pygame.display.set_icon(res.logo)

	# initialize screens
	main_menu_screen = Main_menu_screen(pygame, res, windowSurface)
	game_screen = Game_screen(pygame, res, windowSurface, size, game_clock, game_manager)
	settings_screen = Settings_screen(pygame, res, windowSurface)
	game_over_screen = Game_over_screen(pygame, res, windowSurface, game_manager)
	tutorial_screen = Tutorial_screen(pygame, res, windowSurface)
	credits_screen = Credits_screen(pygame, res, windowSurface)
	game_mode_screen = Game_Mode_Screen(pygame , res , windowSurface , game_manager)


	# game loop starts
	while True:
		events = pygame.event.get()
		game_manager.input.update(events)

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

		elif game_mode == Game_mode.GAME_MODE:
			game_mode = game_mode_screen.update(events)

		else:
			pygame.quit()
			sys.exit()

		game_clock.tick(60)


if __name__ == "__main__":
	game_loop()
