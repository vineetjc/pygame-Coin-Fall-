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
        self.BGCOLOR = (4, 145, 145)
        self.BUTTONCOLOR = (150, 0, 0)

        # images
        # convert for easy blitting
        self.cart_img = pygame.image.load('Images/bb.jpg').convert()
        self.coin_img = pygame.image.load('Images/coin.jpg').convert()
        self.bluecoin = pygame.image.load('Images/bluecoin.jpg').convert()
        self.bomb = pygame.image.load('Images/bomb.png').convert()
        self.R = random.randint(1, 4)
        self.BG = pygame.image.load('Images/coinfallbg'+str(self.R)+'.jpg').convert()
        self.EBG = pygame.image.load('Images/endbg.png').convert()

        # load images for animation

        self.gold_coin_images = [
            pygame.image.load('Images/GoldCoinAnimation/coin1.png').convert_alpha(),
            pygame.image.load('Images/GoldCoinAnimation/coin2.png').convert_alpha(),
            pygame.image.load('Images/GoldCoinAnimation/coin3.png').convert_alpha(),
            pygame.image.load('Images/GoldCoinAnimation/coin4.png').convert_alpha(),
            pygame.image.load('Images/GoldCoinAnimation/coin5.png').convert_alpha(),
            pygame.image.load('Images/GoldCoinAnimation/coin6.png').convert_alpha()
        ]

        self.silver_coin_images = [
            pygame.image.load('Images/SilverCoinAnimation/coin1.png').convert_alpha(),
            pygame.image.load('Images/SilverCoinAnimation/coin2.png').convert_alpha(),
            pygame.image.load('Images/SilverCoinAnimation/coin3.png').convert_alpha(),
            pygame.image.load('Images/SilverCoinAnimation/coin4.png').convert_alpha(),
            pygame.image.load('Images/SilverCoinAnimation/coin5.png').convert_alpha(),
            pygame.image.load('Images/SilverCoinAnimation/coin6.png').convert_alpha()
        ]
