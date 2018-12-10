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
        self.BUTTONCOLOR = (202, 84, 36)

        # images
        # convert for easy blitting
        self.logo = pygame.image.load('res/images/misc/logo.png').convert_alpha()
        self.cart_img = pygame.image.load('res/images/bg/cart.jpg').convert()
        self.coin_img = pygame.image.load('res/images/bg/coin.jpg').convert()
        self.bluecoin = pygame.image.load('res/images/bg/bluecoin.jpg').convert()
        self.bomb = pygame.image.load('res/images/objects/bomb.png').convert_alpha()
        self.R = random.randint(1, 4)
        self.BG = pygame.image.load('res/images/bg/coinfallbg'+str(self.R)+'.jpg').convert()
        self.EBG = pygame.image.load('res/images/bg/endbg.png').convert()

        # load images for animation

        self.gold_coin_images = [
            pygame.image.load('res/images/objects/GoldCoinAnimation/coin1.png').convert_alpha(),
            pygame.image.load('res/images/objects/GoldCoinAnimation/coin2.png').convert_alpha(),
            pygame.image.load('res/images/objects/GoldCoinAnimation/coin3.png').convert_alpha(),
            pygame.image.load('res/images/objects/GoldCoinAnimation/coin4.png').convert_alpha(),
            pygame.image.load('res/images/objects/GoldCoinAnimation/coin5.png').convert_alpha(),
            pygame.image.load('res/images/objects/GoldCoinAnimation/coin6.png').convert_alpha()
        ]

        self.silver_coin_images = [
            pygame.image.load('res/images/objects/SilverCoinAnimation/coin1.png').convert_alpha(),
            pygame.image.load('res/images/objects/SilverCoinAnimation/coin2.png').convert_alpha(),
            pygame.image.load('res/images/objects/SilverCoinAnimation/coin3.png').convert_alpha(),
            pygame.image.load('res/images/objects/SilverCoinAnimation/coin4.png').convert_alpha(),
            pygame.image.load('res/images/objects/SilverCoinAnimation/coin5.png').convert_alpha(),
            pygame.image.load('res/images/objects/SilverCoinAnimation/coin6.png').convert_alpha()
        ]
