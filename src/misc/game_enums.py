from enum import Enum


class Game_Mode(Enum):
    ''' Enum used to decide which screen to show in the main game loop. '''
    MAIN_MENU = 1
    CLASSIC = 2
    SETTINGS = 3
    GAME_OVER = 4
    TUTORIAL = 5
    CREDITS = 6
    GAME_MODE = 7
    INTRODUCTION = 8
    INFINITE = 9
    ONE_V_ONE = 10
    AI = 11
    HARDCORE = 12
    HEIST = 13
    QUIT = 14


class Entity(Enum):
    ''' Enum to differentiate between various game entities. '''
    COIN = 1
    BLUE_COIN = 2
    BOMB = 3
    CART = 4
