##########################################
# Load all the resources used by the game
##########################################
import random


class Resources:

    def __init__(self, pygame):

        # set up fonts
        # None is for default system font
        self.basicFont = pygame.font.SysFont(None, 48)
        self.game_title_font = pygame.font.Font('res/fonts/have-nothing-to-do-with.regular.ttf', 130)
        self.heading1_font = pygame.font.Font('res/fonts/RussoOne-Regular.ttf', 64)
        self.heading2_font = pygame.font.Font('res/fonts/RussoOne-Regular.ttf', 48)
        self.heading3_font = pygame.font.Font('res/fonts/RussoOne-Regular.ttf', 38)
        self.body_font = pygame.font.Font('res/fonts/Economica-Regular.ttf', 28)
        self.button_font = pygame.font.Font('res/fonts/Weston Free.otf', 32)
        self.button_font2 = pygame.font.Font('res/fonts/Economica-Bold.ttf', 38)
        self.button_font3 = pygame.font.Font('res/fonts/alba.regular.ttf', 40)
        self.score_font = pygame.font.Font('res/fonts/Economica-Bold.ttf', 36)

        # set colors R, G, B code
        self.BLACK =                    (0, 0, 0)
        self.WHITE =                    (255, 255, 255)
        self.BGCOLOR =                  (4, 145, 145)
        self.button_color =             (202, 84, 36)
        self.button_text_color =        (43, 17, 0)
        self.game_title_text_color =    (255, 204, 0)
        self.heading1_text_color =      (255, 255, 255)
        self.heading2_text_color =      (255, 255, 255)
        self.heading3_text_color =      (255, 255, 255)
        self.body_text_color =          (255, 255, 255)
        self.score_text_color =         (61, 24, 0)

        # images
        # convert for easy blitting
        self.logo = pygame.image.load(
            'res/images/misc/logo.png').convert_alpha()
        self.cart_img = pygame.image.load(
            'res/images/bg/cart.jpg').convert()
        self.coin_img = pygame.image.load(
            'res/images/bg/coin.jpg').convert()
        self.bluecoin = pygame.image.load(
            'res/images/bg/bluecoin.jpg').convert()
        self.bomb = pygame.image.load(
            'res/images/objects/bomb.png').convert_alpha()
        self.R = random.randint(1, 4)
        self.BG = pygame.image.load(
            'res/images/bg/coinfallbg'+str(self.R)+'.jpg').convert()
        self.EBG = pygame.image.load(
            'res/images/bg/endbg3.png').convert()
        self.button_image_size = (227, 62)
        self.button_image = pygame.image.load(
            'res/images/ui/Lumber_no_text.png').convert_alpha()
        self.score_bg_image_size = (236, 69)
        self.score_bg_image = pygame.image.load(
            'res/images/ui/Connect_less_no_text.png').convert_alpha()

        # load images for animation

        self.gold_coin_images = [
            pygame.image.load(
                'res/images/objects/GoldCoinAnimation/coin1.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/GoldCoinAnimation/coin2.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/GoldCoinAnimation/coin3.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/GoldCoinAnimation/coin4.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/GoldCoinAnimation/coin5.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/GoldCoinAnimation/coin6.png').convert_alpha()
        ]

        self.silver_coin_images = [
            pygame.image.load(
                'res/images/objects/SilverCoinAnimation/coin1.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/SilverCoinAnimation/coin2.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/SilverCoinAnimation/coin3.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/SilverCoinAnimation/coin4.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/SilverCoinAnimation/coin5.png').convert_alpha(),
            pygame.image.load(
                'res/images/objects/SilverCoinAnimation/coin6.png').convert_alpha()
        ]
