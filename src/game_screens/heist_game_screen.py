import random
import math

from pygame.locals import QUIT, KEYUP
from src.game_screens.screen import Screen
from src.game_screens.classic_game_screen import Classic_Game_Screen
from src.misc.game_enums import Game_Mode
from src.ui.image import Image
from src.ui.text import Text

from src.objects import *


class Heist_Game_Screen(Classic_Game_Screen):
    def __init__(self, pygame, res, surface, size, gameclock, game_manager):
        Classic_Game_Screen.__init__(self, pygame, res, surface,
                             size, gameclock, game_manager)
