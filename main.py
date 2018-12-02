######################################
# - Fix Basic syntax
# - Port to Python3
# - Add Game Restart
######################################
import pygame
import sys
import random
import math

from pygame.locals import QUIT, KEYUP
from src.resources import Resources
from src.cart import Cart
from src.coin import Coin
from src.bluecoin import BlueCoin
from src.bomb import Bomb

pygame.init()

# setup the window display
size = (1024, 768)
windowSurface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('Super Mumbo Epicness')

# initialize resources
res = Resources(pygame)


def coinGame():  # Renamed from CoinGame to coinGame
    result = 0
    i = 1
    coinlist = []
    gameclock = pygame.time.Clock()
    timer = 0
    cart = Cart(res, size)

    # Set up texts
    time_text = res.basicFont.render('TIMER:', True, res.BLACK, res.WHITE)
    textbox = time_text.get_rect(center=(900, 170))
    point_text = res.basicFont.render('POINTS:', True, res.BLACK, res.WHITE)
    pointbox = point_text.get_rect(center=(100, 170))
    display_time = res.basicFont.render('0', True, res.BLACK, res.WHITE)
    timebox = display_time.get_rect(center=(900, 200))
    score = res.basicFont.render(str(cart.points), True, res.BLACK, res.WHITE)
    scorebox = score.get_rect(center=(100, 200))

    # Add a restart text
    restart = res.basicFont.render(
        'Press R to restart!', True, res.BLACK, res.WHITE)
    restartbox = restart.get_rect(center=(512, 384))

    over = False

    while True:  # Changed to infinite loop
        if timer > 30 or cart.dead:
            over = True

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Add a restart key
            elif event.type == KEYUP:
                if event.key == pygame.K_r and (cart.dead or over):
                    over = False
                    time_text = res.basicFont.render(
                        'TIMER:', True, res.BLACK, res.WHITE)
                    cart = Cart(res, size)
                    timer = 0
                    coinlist = []
                    i = 1

        if not over:
            cart.handle_keys(pygame, size)
            windowSurface.blit(pygame.transform.scale(res.BG, size), (0, 0))
            cart.draw(windowSurface)

            # randomizing bonus coin/bomb/coin fall frequency, can change this
            if not i % 3 or not i % 4:
                select = random.randint(1, 2)
                if select == 1:
                    c = BlueCoin(res, size)  # Changed C to c
                else:  # Remove redundant check
                    c = Bomb(res, size)
            elif not i % 5 or not i % 7 or not i % 11:
                c = Bomb(res, size)
            else:
                c = Coin(res, size)

            coinlist.append(c)

            for b in coinlist[0:i:15]:
                # (use 14 or 15) this is for the rate at which
                # objects fall, can change this
                b.draw(windowSurface)
                b.fall()
                cart.collect_item(pygame, res, b)

    # pygame.display.flip() #Redundant call
            i += 1

        # Update time
        seconds = gameclock.tick(30)/1000.0
        timer += seconds
        # returns real value of timer to int value
        int_timer = math.trunc(timer)
        if int_timer < 30 and not (cart.dead or over):
            display_time = res.basicFont.render(
                str(int_timer), True, res.BLACK, res.WHITE)
            windowSurface.blit(display_time, timebox)
        else:  # Removed redundant check
            time_text = res.basicFont.render(
                'TIME UP!', True, res.BLACK, res.WHITE)
        windowSurface.blit(time_text, textbox)
        windowSurface.blit(point_text, pointbox)
        score = res.basicFont.render(
            str(cart.points), True, res.BLACK, res.WHITE)
        windowSurface.blit(score, scorebox)

        # Add a restart display if dead or timeup
        if cart.dead or over:
            windowSurface.blit(restart, restartbox)

        pygame.display.flip()
    pygame.time.delay(500)
    pygame.quit()
    return


if __name__ == "__main__":
    coinGame()
