from enum import Enum


class Game_mode(Enum):
    ''' Enum used to decide which screen to show in the main game loop. '''
    MAIN_MENU = 1
    GAME = 2
    SETTINGS = 3
    GAME_OVER = 4
    TUTORIAL = 5
    CREDITS = 6
    QUIT = 7


class Entity(Enum):
    ''' Enum to differentiate between various game entities. '''
    COIN = 1
    BLUE_COIN = 2
    BOMB = 3
    CART = 4
