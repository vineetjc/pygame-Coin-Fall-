import random
import math

from pygame.locals import QUIT, KEYUP
from src.game_screens.screen import Screen
from src.game_screens.game_screen import Game_screen
from src.misc.game_enums import Game_mode
from src.ui.image import Image
from src.ui.text import Text

from src.objects import *


class Heist_Game_Screen(Game_screen):
    def __init__(self, pygame, res, surface, size, gameclock, game_manager):
        Game_screen.__init__(self, pygame, res, surface,
                             size, gameclock, game_manager)
