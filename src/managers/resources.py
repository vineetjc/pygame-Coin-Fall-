##########################################
# Load all the resources used by the game
##########################################
import random


class Resources:

    def __init__(self, pygame, size):

        # set up fonts
        # None is for default system font
        self.basicFont = pygame.font.SysFont(None, 48)
        self.game_title_font = pygame.font.Font(
            'res/fonts/have-nothing-to-do-with.regular.ttf', 130)
        self.heading1_font = pygame.font.Font(
            'res/fonts/RussoOne-Regular.ttf', 64)
        self.heading2_font = pygame.font.Font(
            'res/fonts/RussoOne-Regular.ttf', 48)
        self.heading3_font = pygame.font.Font(
            'res/fonts/RussoOne-Regular.ttf', 38)
        self.body_font = pygame.font.Font(
            'res/fonts/Economica-Regular.ttf', 28)
        self.button_font = pygame.font.Font('res/fonts/Weston Free.otf', 32)
        self.button_font2 = pygame.font.Font(
            'res/fonts/Economica-Bold.ttf', 38)
        self.button_font3 = pygame.font.Font('res/fonts/alba.regular.ttf', 40)
        self.score_font = pygame.font.Font('res/fonts/Economica-Bold.ttf', 36)

        # set colors R, G, B code
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BGCOLOR = (4, 145, 145)
        self.button_color = (202, 84, 36)
        self.button_text_color = (43, 17, 0)
        self.game_title_text_color = (255, 204, 0)
        self.heading1_text_color = (255, 255, 255)
        self.heading2_text_color = (255, 255, 255)
        self.heading3_text_color = (255, 255, 255)
        self.body_text_color = (255, 255, 255)
        self.score_text_color = (61, 24, 0)

        # images
        # convert for easy blitting
        self.logo = pygame.image.load(
            'res/images/misc/logo.png').convert_alpha()
        self.cart_img = pygame.image.load(
            'res/images/objects/cart_new.png').convert_alpha()
        self.cart_player1_img = pygame.image.load(
            'res/images/objects/cart_player1.png').convert_alpha()
        self.cart_player2_img = pygame.image.load(
            'res/images/objects/cart_player2.png').convert_alpha()
        self.cart_ai_img = pygame.image.load(
            'res/images/objects/cart_ai.png').convert_alpha()
        self.coin_img = pygame.image.load(
            'res/images/bg/coin.jpg').convert()
        self.bluecoin = pygame.image.load(
            'res/images/bg/bluecoin.jpg').convert()
        self.bomb = pygame.image.load(
            'res/images/objects/bomb.png').convert_alpha()

        self.set_random_bg(pygame, size)

        self.EBG = pygame.image.load(
            'res/images/bg/endbg3.png').convert()
        self.button_image_size = (227, 62)
        self.button_image = pygame.image.load(
            'res/images/ui/Lumber_no_text.png').convert_alpha()
        self.score_bg_image_size = (236, 69)
        self.score_bg_image = pygame.image.load(
            'res/images/ui/Connect_less_no_text.png').convert_alpha()

        # animation sprites
        self.silver_coin_anim_size = 64
        self.silver_coin_anim = []
        for i in range(1, 7):
            frame = pygame.image.load(
                'res/images/objects/SilverCoinAnimation/coin' + str(i) + '.png').convert_alpha()
            frame = pygame.transform.scale(
                frame, (self.silver_coin_anim_size, self.silver_coin_anim_size))
            self.silver_coin_anim.append(frame)

        self.gold_coin_anim_size = 64
        self.gold_coin_anim = []
        for i in range(1, 7):
            frame = pygame.image.load(
                'res/images/objects/GoldCoinAnimation/coin' + str(i) + '.png').convert_alpha()
            frame = pygame.transform.scale(
                frame, (self.gold_coin_anim_size, self.gold_coin_anim_size))
            self.gold_coin_anim.append(frame)

        self.bomb_anim_size = 64
        self.bomb_anim = []
        frame = pygame.image.load(
            'res/images/objects/bomb.png').convert_alpha()
        frame = pygame.transform.scale(
            frame, (self.bomb_anim_size, self.bomb_anim_size))
        self.bomb_anim.append(frame)

        self.blast_anim1_size = 240
        self.blast_anim1 = []
        for i in range(0, 15):
            frame = pygame.image.load(
                'res/images/objects/blast1/tile' + str(i).rjust(3, '0') + '.png').convert_alpha()
            frame = pygame.transform.scale(
                frame, (self.blast_anim1_size, self.blast_anim1_size))
            self.blast_anim1.append(frame)

        self.blast_anim2_size = 60
        self.blast_anim2 = []
        for i in range(0, 8):
            frame = pygame.image.load(
                'res/images/objects/blast2/tile' + str(i).rjust(3, '0') + '.png').convert_alpha()
            frame = pygame.transform.scale(
                frame, (self.blast_anim2_size, self.blast_anim2_size))
            self.blast_anim2.append(frame)

        self.blast_anim3_size = 60
        self.blast_anim3 = []
        for i in range(0, 8):
            frame = pygame.image.load(
                'res/images/objects/blast3/tile' + str(i).rjust(3, '0') + '.png').convert_alpha()
            frame = pygame.transform.scale(
                frame, (self.blast_anim3_size, self.blast_anim3_size))
            self.blast_anim3.append(frame)

    def set_random_bg(self, pygame, size):
        self.R = random.randint(1, 4)
        self.BG = pygame.image.load(
            'res/images/bg/coinfallbg'+str(self.R)+'.jpg').convert()
        self.BG = pygame.transform.scale(self.BG, size)
