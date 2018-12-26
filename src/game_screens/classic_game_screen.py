import random
import math

from pygame.locals import QUIT, KEYUP
from src.game_screens.screen import Screen
from src.misc.game_enums import Game_Mode, Entity
from src.ui.image import Image
from src.ui.text import Text

from src.objects import *


class Classic_Game_Screen(Screen):
    def __init__(self, pygame, res, surface, size, gameclock, game_manager):
        Screen.__init__(self, pygame, res, surface, size)

        score_x, score_y = res.score_bg_image_size

        self.images['ScoreBG'] = Image(
            pygame, res, surface, (0, 0), res.score_bg_image)
        self.images['TimeBG'] = Image(
            pygame, res, surface, (self.center_x * 2 - score_x, 0), res.score_bg_image)

        self.texts['Score'] = Text(
            pygame, res, surface, (45, score_y / 2), 'Score: 30', res.score_font, res.score_text_color, alignment='left')

        self.texts['Time'] = Text(
            pygame, res, surface, (self.center_x * 2 - score_x / 2 - 65, score_y / 2), 'Time: 50', res.score_font, res.score_text_color, alignment='left')

        self.game_over_text1 = Text(
            pygame, res, surface, (self.center_x + 3, self.center_y + 3), 'GAME OVER', res.game_title_font, res.BLACK)

        self.game_over_text2 = Text(
            pygame, res, surface, (self.center_x, self.center_y), 'GAME OVER', res.game_title_font, res.game_title_text_color)

        # set up initial variables
        self.need_reset = False
        self.size = size
        self.result = 0
        self.coinlist = []
        self.gameclock = gameclock
        self.game_manager = game_manager
        self.game_manager.score = 0
        self.timer = 0
        self.cart = Cart(res, self.size, surface, self.game_manager)
        self.animation_manager = game_manager.animation_manager
        self.waiting_death_explosion = False
        self.wait_death_timer = 0
        self.wait_death_time = 100
        self.spawn_pos_x = self.size[0] / 2
        self.death_zone = Death_Zone(self.size)
        self.res.set_random_bg(self.pygame, self.size)

    def reset_before_restart(self):
        self.need_reset = False
        self.result = 0
        self.coinlist = []
        self.game_manager.score = 0
        self.timer = 0
        self.game_manager.reset()
        self.cart = Cart(self.res, self.size, self.surface, self.game_manager)
        self.animation_manager.remove_all_animations()
        self.waiting_death_explosion = False
        self.wait_death_timer = 0
        self.res.set_random_bg(self.pygame, self.size)

    def update(self, events):
        # if we are restarting the game
        if self.need_reset:
            self.reset_before_restart()

        # if watiting after death for explosion animation to get over
        if self.waiting_death_explosion:
            self.surface.blit(self.res.BG, (0, 0))
            self.cart.draw()
            self.game_over_text1.draw()
            self.game_over_text2.draw()
            self.animation_manager.draw_animations()
            self.wait_death_timer += 1

            if self.wait_death_timer > self.wait_death_time:
                self.need_reset = True
                return Game_Mode.GAME_OVER
            else:
                return Game_Mode.CLASSIC

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

            if self.cart.check_collision(coin):
                self.scoring_function(coin)

            if self.death_zone.check_collision(coin):
                self.coinlist.remove(coin)
                del coin

        self.cart.move()
        self.cart.draw()

        self.animation_manager.draw_animations()

        # Update time
        seconds = self.gameclock.get_time() / 1000.0
        self.timer += seconds

        # returns real value of timer to int value
        int_timer = math.trunc(self.timer)
        self.texts['Score'].change_text(
            'Score: ' + str(int(self.game_manager.score)))
        self.texts['Time'].change_text('Time: ' + str(int_timer))

        if self.timer > 30 or self.cart.dead:
            self.game_manager.score = int(self.game_manager.score)
            self.waiting_death_explosion = True

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.CLASSIC

    def get_random_entity(self):

        if random.random() < self.params['spawn_chance']:

            coin_select_random = random.random()
            self.pick_new_spawn_pos_x()

            if coin_select_random < self.params['silver_chance']:
                return Coin(self.res, self.size, self.surface, self.spawn_pos_x, -50)
            elif coin_select_random < (self.params['silver_chance'] + self.params['gold_chance']):
                return BlueCoin(self.res, self.size, self.surface, self.spawn_pos_x, -50)
            else:
                return Bomb(self.res, self.size, self.surface, self.spawn_pos_x, -50)

        else:
            return None

    def pick_new_spawn_pos_x(self):
        new_rand = random.randint(50, self.size[0] - 50)

        # to prevent overlapping spawn
        if abs(new_rand - self.spawn_pos_x) < 50:
            self.pick_new_spawn_pos_x()
        else:
            self.spawn_pos_x = new_rand

    def scoring_function(self, coin):
        if coin.collected:
            return

        if coin.type == Entity.BLUE_COIN:
            self.game_manager.score += 3 * self.params['score_multiplier']
            self.animation_manager.create_new_effect(
                self.res.blast_anim3, self.res.blast_anim3_size, 4, False, coin.collision_rect().midbottom)

        elif coin.type == Entity.COIN:
            self.game_manager.score += 1 * self.params['score_multiplier']
            self.animation_manager.create_new_effect(
                self.res.blast_anim2, self.res.blast_anim2_size, 4, False, coin.collision_rect().midbottom)

        else:
            self.cart.dead = True
            self.animation_manager.create_new_effect(
                self.res.blast_anim1, self.res.blast_anim1_size, 4, False, coin.collision_rect().midbottom)

        coin.collect()
