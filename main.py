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

pygame.init()

#setup the window display
size = (1024, 768)
windowSurface  = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('Super Mumbo Epicness')

# set up fonts
basicFont = pygame.font.SysFont(None, 48) #None is for default system font

#set colors R, G, B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#images
#convert for easy blitting
cart_img = pygame.image.load('Images/bb.jpg').convert()
coin_img = pygame.image.load('Images/coin.jpg').convert()
bluecoin = pygame.image.load('Images/bluecoin.jpg').convert()
bomb = pygame.image.load('Images/bomb.png').convert()
R = random.randint(1, 4)
BG = pygame.image.load('Images/coinfallbg'+str(R)+'.jpg').convert()


class Cart(object):
    def __init__(self):
        self.image = cart_img
        self.x = (size[0] / 2) - 80
        self.y = size[1] - 120
        self.points = 0 #Changed Points to points
        self.dead = False #Add this for game end check


    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 10 #Change this value if necessary
        if key[pygame.K_RIGHT]:
            if self.x < size[0] - 140:
                self.x += dist
                
            else: #Removed redundant condition
                pass
              
        elif key[pygame.K_LEFT]:
            if self.x > -10:
                self.x -= dist
            else:
                pass

            
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


    def collect_item(self, coin):
        if 645 > coin.y > 633:
            if ((self.x < coin.x + (55.0 / 2) < self.x + 160) and
                (self.x < coin.x) and (self.x + 160 > coin.x + 55)):
                try:
                    if coin.image == bluecoin:
                        self.points += 3 #Bonus coin
                    elif coin.image == bomb:
                        pygame.time.delay(500)
                        self.dead = True #Replace quit with death
##                        pygame.quit()
##                        sys.exit()
                    else:
                        self.points += 1
                    del coin.image
                except AttributeError:
                    pass


class Coin():
    def __init__(self):
        self.image = coin_img
        self.x = random.randint(0, size[0] - 55)
        self.y = -15


    def fall(self):
        self.y += 7 #Change the value if necessary


    def draw(self, surface):
        try:
            surface.blit(self.image, (self.x, self.y))
        except AttributeError:
            pass


class BlueCoin(Coin): #bonus coin
    def __init__(self):
        Coin.__init__(self)
        self.image = bluecoin


class Bomb(Coin):
    def __init__(self):
        Coin.__init__(self)
        self.image = bomb
        
        
def coinGame(): #Renamed from CoinGame to coinGame
    result = 0
    i = 1
    coinlist = []
    gameclock = pygame.time.Clock()
    timer = 0
    cart = Cart()

    #Set up texts
    time_text = basicFont.render('TIMER:', True, BLACK, WHITE)
    textbox = time_text.get_rect(center=(900, 170))
    point_text = basicFont.render('POINTS:', True, BLACK, WHITE)
    pointbox = point_text.get_rect(center=(100, 170))
    display_time = basicFont.render('0', True, BLACK, WHITE)
    timebox = display_time.get_rect(center=(900, 200))
    score = basicFont.render(str(cart.points), True, BLACK, WHITE)
    scorebox = score.get_rect(center=(100, 200))

    #Add a restart text
    restart = basicFont.render('Press R to restart!', True, BLACK, WHITE)
    restartbox = restart.get_rect(center=(512, 384))

    over = False

    while True: #Changed to infinite loop
        if timer > 30 or cart.dead:
            over = True
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Add a restart key
            elif event.type == KEYUP:
                if event.key == pygame.K_r and (cart.dead or over):
                    over = False
                    time_text = basicFont.render('TIMER:', True, BLACK, WHITE)
                    cart = Cart()
                    timer = 0
                    coinlist = []
                    i = 1

        if not over:
            cart.handle_keys()
            windowSurface.blit(pygame.transform.scale(BG, size), (0, 0))
            cart.draw(windowSurface)

            #randomizing bonus coin/bomb/coin fall frequency, can change this
            if not i%3 or not i%4:
                select = random.randint(1, 2)
                if select == 1:
                    c = BlueCoin() #Changed C to c
                else: #Remove redundant check
                    c = Bomb()
            elif not i%5 or not i%7 or not i%11:
                c = Bomb()
            else:
                c = Coin()

            coinlist.append(c)

            for b in coinlist[0:i:15]:
                #(use 14 or 15) this is for the rate at which
                #objects fall, can change this
                b.draw(windowSurface)
                b.fall()
                cart.collect_item(b)

    ##        pygame.display.flip() #Redundant call
            i += 1

        #Update time
        seconds = gameclock.tick(30)/1000.0
        timer += seconds
        int_timer = math.trunc(timer) #returns real value of timer to int value
        if int_timer < 30 and not (cart.dead or over):
            display_time = basicFont.render(str(int_timer), True, BLACK, WHITE)
            windowSurface.blit(display_time, timebox)
        else: #Removed redundant check
            time_text = basicFont.render('TIME UP!', True, BLACK, WHITE)
        windowSurface.blit(time_text, textbox)
        windowSurface.blit(point_text, pointbox)
        score = basicFont.render(str(cart.points), True, BLACK, WHITE)
        windowSurface.blit(score, scorebox)

        #Add a restart display if dead or timeup
        if cart.dead or over:
            windowSurface.blit(restart, restartbox)
        
        pygame.display.flip()
    pygame.time.delay(500)
    pygame.quit()
    return
  

if __name__ == "__main__":
    coinGame()
