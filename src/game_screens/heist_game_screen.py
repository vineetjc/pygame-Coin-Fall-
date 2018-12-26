import random
import math

from pygame.locals import QUIT, KEYUP
from src.game_screens.screen import Screen
from src.game_screens.classic_game_screen import Classic_Game_Screen
from src.misc.game_enums import Game_Mode, Entity
from src.ui.image import Image
from src.ui.text import Text

from src.objects import *


class Heist_Game_Screen(Classic_Game_Screen):
    def __init__(self, pygame, res, surface, size, gameclock, game_manager):
        Classic_Game_Screen.__init__(self, pygame, res, surface,
                                     size, gameclock, game_manager)

        score_x, score_y = res.score_bg_image_size

        self.images['Misses_BG'] = Image(
            pygame, res, surface, (0, score_y), res.score_bg_image)

        self.texts['Misses'] = Text(
            pygame, res, surface, (45, score_y + score_y / 2), 'Misses: 0', res.score_font, res.score_text_color, alignment='left')

        self.misses_in_row = 0

    def reset_before_restart(self):
        Classic_Game_Screen.reset_before_restart(self)
        self.misses_in_row = 0

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
                return Game_Mode.HEIST

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
                self.misses_in_row += 1
                if self.misses_in_row > 3:
                    self.cart.dead = True
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
        self.texts['Misses'].change_text('Misses: ' + str(self.misses_in_row))

        if self.timer > 30 or self.cart.dead:
            self.game_manager.score = int(self.game_manager.score)
            self.waiting_death_explosion = True

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.HEIST

    def scoring_function(self, coin):
        if coin.collected:
            return

        self.misses_in_row = 0

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
