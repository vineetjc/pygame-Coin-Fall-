import random
import math

from pygame.locals import QUIT, KEYUP
from src.game_screens.infinite_game_screen import Infinite_Game_Screen
from src.misc.game_enums import Game_Mode
from src.ui.image import Image
from src.ui.text import Text

from src.objects import *


class Hardcore_Game_Screen(Infinite_Game_Screen):
    def __init__(self, pygame, res, surface, size, gameclock, game_manager):
        Infinite_Game_Screen.__init__(self, pygame, res, surface,
                             size, gameclock, game_manager)
