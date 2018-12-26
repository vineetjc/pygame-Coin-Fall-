import random
import math

from pygame.locals import QUIT, KEYUP
from src.game_screens.screen import Screen
from src.game_screens.classic_game_screen import Classic_Game_Screen
from src.misc.game_enums import Game_Mode, Entity
from src.ui.image import Image
from src.ui.text import Text

from src.objects import *


class One_V_One_Game_Screen(Classic_Game_Screen):
    def __init__(self, pygame, res, surface, size, gameclock, game_manager):
        Classic_Game_Screen.__init__(self, pygame, res, surface,
                                     size, gameclock, game_manager)

        score_x, score_y = res.score_bg_image_size

        self.images = {}
        self.texts = {}

        self.images['ScoreBG_Player1'] = Image(
            pygame, res, surface, (0, 0), res.score_bg_image)

        self.images['ScoreBG_Player2'] = Image(
            pygame, res, surface, (0, score_y), res.score_bg_image)

        self.texts['Score_Player1'] = Text(
            pygame, res, surface, (45, score_y / 2), 'Player 1: 30', res.score_font, res.score_text_color, alignment='left')

        self.texts['Score_Player2'] = Text(
            pygame, res, surface, (45, score_y + score_y / 2), 'Player 2: 30', res.score_font, res.score_text_color, alignment='left')

        self.images['TimeBG'] = Image(
            pygame, res, surface, (self.center_x * 2 - score_x, 0), res.score_bg_image)

        self.texts['Time'] = Text(
            pygame, res, surface, (self.center_x * 2 - score_x / 2 - 65, score_y / 2), 'Time: 50', res.score_font, res.score_text_color, alignment='left')

        self.cart_player1 = Cart_One_V_One(
            res, size, surface, game_manager, res.cart_player1_img, 'horizontal_player1', -100)
        self.cart_player2 = Cart_One_V_One(
            res, size, surface, game_manager, res.cart_player2_img, 'horizontal_player2', 100)
        self.score_player1 = 0
        self.score_player2 = 0

    def reset_before_restart(self):
        Classic_Game_Screen.reset_before_restart(self)

        self.cart_player1 = Cart_One_V_One(
            self.res, self.size, self.surface, self.game_manager, self.res.cart_player1_img, 'horizontal_player1', -100)
        self.cart_player2 = Cart_One_V_One(
            self.res, self.size, self.surface, self.game_manager, self.res.cart_player2_img, 'horizontal_player2', 100)
        self.score_player1 = 0
        self.score_player2 = 0

    def update(self, events):
        # if we are restarting the game
        if self.need_reset:
            self.reset_before_restart()

        # if watiting after death for explosion animation to get over
        if self.waiting_death_explosion:
            self.surface.blit(self.res.BG, (0, 0))
            self.cart_player1.draw()
            self.cart_player2.draw()
            self.game_over_text1.draw()
            self.game_over_text2.draw()

            self.animation_manager.draw_animations()
            self.wait_death_timer += 1

            if self.wait_death_timer > self.wait_death_time:
                self.need_reset = True
                return Game_Mode.GAME_OVER
            else:
                return Game_Mode.ONE_V_ONE

        self.params = self.game_manager.params

        self.surface.blit(self.res.BG, (0, 0))

        for image in self.images:
            self.images[image].draw()

        for text in self.texts:
            self.texts[text].draw()

        coin = self.get_random_entity()
        if coin is not None:
            self.coinlist.append(coin)

        # drawing coins and checking coin collisions
        for coin in self.coinlist:
            coin.draw()
            coin.fall()

            if self.cart_player1.check_collision(coin):
                self.scoring_function(coin, self.score_player1, True)

            if self.cart_player2.check_collision(coin):
                self.scoring_function(coin, self.score_player2, False)

            if self.death_zone.check_collision(coin):
                self.coinlist.remove(coin)
                del coin

        self.cart_player1.move()
        self.cart_player1.draw()

        self.cart_player2.move()
        self.cart_player2.draw()

        self.animation_manager.draw_animations()

        # Update time
        seconds = self.gameclock.get_time() / 1000.0
        self.timer += seconds

        # returns real value of timer to int value
        int_timer = math.trunc(self.timer)
        self.texts['Score_Player1'].change_text(
            'Player 1: ' + str(int(self.score_player1)))

        self.texts['Score_Player2'].change_text(
            'Player 2: ' + str(int(self.score_player2)))

        self.texts['Time'].change_text('Time: ' + str(int_timer))

        if self.timer > 30 or self.cart_player1.dead or self.cart_player2.dead:
            self.game_manager.score = int(self.game_manager.score)
            self.waiting_death_explosion = True

            if self.cart_player1.dead:
                self.game_over_text1.change_text('PLAYER 2 WINS')
                self.game_over_text2.change_text('PLAYER 2 WINS')
            else:
                self.game_over_text1.change_text('PLAYER 1 WINS')
                self.game_over_text2.change_text('PLAYER 1 WINS')

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.ONE_V_ONE

    def scoring_function(self, coin, score, is_player1):
        if coin.collected:
            return

        if coin.type == Entity.BLUE_COIN:
            if is_player1:
                self.score_player1 += 3 * self.params['score_multiplier']
            else:
                self.score_player2 += 3 * self.params['score_multiplier']

            self.animation_manager.create_new_effect(
                self.res.blast_anim3, self.res.blast_anim3_size, 4, False, coin.collision_rect().midbottom)

        elif coin.type == Entity.COIN:
            if is_player1:
                self.score_player1 += 1 * self.params['score_multiplier']
            else:
                self.score_player2 += 1 * self.params['score_multiplier']

            self.animation_manager.create_new_effect(
                self.res.blast_anim2, self.res.blast_anim2_size, 4, False, coin.collision_rect().midbottom)

        else:
            if is_player1:
                self.cart_player1.dead = True
            else:
                self.cart_player2.dead = True
            self.animation_manager.create_new_effect(
                self.res.blast_anim1, self.res.blast_anim1_size, 4, False, coin.collision_rect().midbottom)

        coin.collect()
