import random
import math

from pygame.locals import QUIT, KEYUP
from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode
from src.ui.image import Image
from src.ui.text import Text

from src.objects.cart import Cart
from src.objects.coin import Coin
from src.objects.bluecoin import BlueCoin
from src.objects.bomb import Bomb


# game_manager=Game_manager()
class Game_screen(Screen):
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

        # set up initial variables
        self.need_reset = False
        self.size = size
        self.result = 0
        self.arbit_var = 1
        self.coinlist = []
        self.gameclock = gameclock
        self.game_manager = game_manager
        self.timer = 0
        self.cart = Cart(res, self.size, surface, self.game_manager)
        self.animation_manager = game_manager.animation_manager
        self.waiting_death_explosion = False
        self.wait_death_timer = 0
        self.wait_death_time = 200

    def reset_before_restart(self):
        self.need_reset = False
        self.result = 0
        self.arbit_var = 1
        self.coinlist = []
        self.timer = 0
        self.game_manager.reset()
        del self.cart
        self.cart = Cart(self.res, self.size, self.surface, self.game_manager)
        self.animation_manager.remove_all_animations()
        self.waiting_death_explosion = False
        self.wait_death_timer = 0

    def update(self, events):
        # if we are restarting the game
        if self.need_reset:
            self.reset_before_restart()

        if self.waiting_death_explosion:
            self.surface.blit(self.pygame.transform.scale(
                self.res.BG, self.size), (0, 0))
            self.cart.draw()
            self.animation_manager.draw_animations()
            self.pygame.display.flip()
            self.wait_death_timer += 1

            if self.wait_death_timer > self.wait_death_time:
                self.need_reset = True
                return Game_mode.GAME_OVER
            else:
                return Game_mode.GAME

        self.cart.move()
        self.surface.blit(self.pygame.transform.scale(
            self.res.BG, self.size), (0, 0))

        for image in self.images:
            self.images[image].draw()

        for text in self.texts:
            self.texts[text].draw()

        c = self.get_random_entity(
            self.arbit_var, self.res, self.size, self.surface)
        self.coinlist.append(c)

        for b in self.coinlist[0:self.arbit_var:self.game_manager.difficulty.value["DENSITY"]]:
            # (use 14 or 15) this is for the rate at which
            # objects fall, can change this
            b.draw()
            b.fall()
            self.cart.collect_item(b)

        self.arbit_var += 1

        self.cart.draw()

        self.animation_manager.draw_animations()

        # Update time
        seconds = self.gameclock.get_time() / 1000.0
        self.timer += seconds

        # returns real value of timer to int value
        int_timer = math.trunc(self.timer)
        self.texts['Score'].change_text('Score: ' + str(self.cart.points))
        self.texts['Time'].change_text('Time: ' + str(int_timer))

        self.pygame.display.flip()

        if self.timer > 30 or self.cart.dead:
            self.game_manager.score = self.cart.points
            self.animation_manager.create_new_effect(
                self.res.blast_anim1, self.res.blast_anim1_size, 0, False, (self.cart.x - 55, self.cart.y - 90))
            self.waiting_death_explosion = True

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.GAME

    def get_random_entity(self, arbit_var, res, size, surface):
        # randomizing bonus coin/bomb/coin fall frequency, can change this
        if not arbit_var % 3 or not arbit_var % 4:
            select = random.randint(1, 2)
            if select == 1:
                c = BlueCoin(res, size, surface)
            else:  # select = 2
                c = Bomb(res, size, surface)
        elif not arbit_var % 5 or not arbit_var % 7 or not arbit_var % 11:
            c = Bomb(res, size, surface)
        else:
            c = Coin(res, size, surface)

        return c
