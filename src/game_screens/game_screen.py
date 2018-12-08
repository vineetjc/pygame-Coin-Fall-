import random
import math

from pygame.locals import QUIT, KEYUP
from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode

from src.objects.cart import Cart
from src.objects.coin import Coin
from src.objects.bluecoin import BlueCoin
from src.objects.bomb import Bomb


class Game_screen(Screen):
    def __init__(self, pygame, res, surface, size, gameclock, game_manager):
        Screen.__init__(self, pygame, res, surface)

        # set up initial variables
        self.need_reset = False
        self.size = size
        self.result = 0
        self.i = 1
        self.coinlist = []
        self.gameclock = gameclock
        self.game_manager = game_manager
        self.timer = 0
        self.cart = Cart(res, self.size, surface)

        # set up texts
        self.time_text = res.basicFont.render('TIMER:', True, res.BLACK, res.WHITE)
        self.textbox = self.time_text.get_rect(center=(900, 170))
        self.point_text = res.basicFont.render('POINTS:', True, res.BLACK, res.WHITE)
        self.pointbox = self.point_text.get_rect(center=(100, 170))
        self.display_time = res.basicFont.render('0', True, res.BLACK, res.WHITE)
        self.timebox = self.display_time.get_rect(center=(900, 200))
        self.score = res.basicFont.render(str(self.cart.points), True, res.BLACK, res.WHITE)
        self.scorebox = self.score.get_rect(center=(100, 200))

    def reset_before_restart(self):
        self.need_reset = False
        self.result = 0
        self.i = 1
        self.coinlist = []
        self.timer = 0
        self.game_manager.reset()
        del self.cart
        self.cart = Cart(self.res, self.size, self.surface)

    def update(self, events):
        # if we are restarting the game
        if self.need_reset:
            self.reset_before_restart()

        self.cart.handle_keys(self.pygame, self.size)
        self.surface.blit(self.pygame.transform.scale(self.res.BG, self.size), (0, 0))

        c = self.get_random_entity(self.i, self.res, self.size, self.surface)
        self.coinlist.append(c)

        for b in self.coinlist[0:self.i:15]:
            # (use 14 or 15) this is for the rate at which
            # objects fall, can change this
            b.draw()
            b.fall()
            self.cart.collect_item(self.pygame, self.res, b)

        self.i += 1

        self.cart.draw()

        # Update time
        seconds = self.gameclock.get_time() / 1000.0
        self.timer += seconds

        # returns real value of timer to int value
        int_timer = math.trunc(self.timer)
        self.display_time = self.res.basicFont.render(str(int_timer), True, self.res.BLACK, self.res.WHITE)    
        self.surface.blit(self.time_text, self.textbox)
        self.surface.blit(self.display_time, self.timebox)
        self.surface.blit(self.point_text, self.pointbox)
        self.score = self.res.basicFont.render(str(self.cart.points), True, self.res.BLACK, self.res.WHITE)
        self.surface.blit(self.score, self.scorebox)

        self.pygame.display.flip()

        if self.timer > 30 or self.cart.dead:
            self.need_reset = True
            self.game_manager.score = self.cart.points
            return Game_mode.GAME_OVER

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.GAME

    def get_random_entity(self, i, res, size, surface):
        # randomizing bonus coin/bomb/coin fall frequency, can change this
        if not i % 3 or not i % 4:
            select = random.randint(1, 2)
            if select == 1:
                c = BlueCoin(res, size, surface)
            else:  # select = 2
                c = Bomb(res, size, surface)
        elif not i % 5 or not i % 7 or not i % 11:
            c = Bomb(res, size, surface)
        else:
            c = Coin(res, size, surface)

        return c
