##########################################
# Load all the resources used by the game
##########################################
import random

class Resources:

    def __init__(self, pygame):

        # set up fonts
        # None is for default system font
        self.basicFont = pygame.font.SysFont(None, 48)

        # set colors R, G, B code
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # images
        # convert for easy blitting
        self.cart_img = pygame.image.load('Images/bb.jpg').convert()
        self.coin_img = pygame.image.load('Images/coin.jpg').convert()
        self.bluecoin = pygame.image.load('Images/bluecoin.jpg').convert()
        self.bomb = pygame.image.load('Images/bomb.png').convert()
        self.R = random.randint(1, 4)
        self.BG = pygame.image.load('Images/coinfallbg'+str(self.R)+'.jpg').convert()
