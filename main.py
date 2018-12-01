import pygame, sys, random, math
from pygame.locals import *

pygame.init()

#setup the window display
size=(1024, 768)
windowSurface = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('Super Mumbo Epicness')

# set up fonts
basicFont = pygame.font.SysFont(None, 48) #none is for default system font, number is size of font

#set colors R, G, B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#images
cart_img = pygame.image.load('Images/bb.jpg')
coin_img = pygame.image.load('Images/coin.jpg')
bluecoin = pygame.image.load('Images/bluecoin.jpg')
bomb = pygame.image.load('Images/bomb.png')
R = random.randint(1, 4)
BG = pygame.image.load('Images/coinfallbg'+str(R)+'.jpg')

class Cart(object):
    def __init__(self):
        self.image = cart_img
        self.x = (size[0]/2)-80
        self.y = size[1]-120
        self.Points = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 10 #change this value if necessary
        if key[pygame.K_RIGHT]:
            if self.x<size[0]-140:
                self.x += dist
        elif key[pygame.K_LEFT]:
            if self.x>-10:
                self.x -= dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def collect_item(self, coin):
        if 645>coin.y>633:
            if self.x<coin.x+(55.0/2)<(self.x+160) and self.x<coin.x and self.x+160>coin.x+55:
                try:
                    if coin.image==bluecoin:
                        self.Points+=3 #bonus coin
                    elif coin.image==bomb:
                        pygame.time.delay(500)
                        pygame.quit()
                        sys.exit()
                    else:
                        self.Points+=1
                    del coin.image
                except AttributeError:
                    pass

class Coin():
    def __init__(self):
        self.image = coin_img
        self.x = random.randint(0, size[0]-55)
        self.y = -15

    def fall(self):
        self.y+=7 #change this value if necessary

    def draw(self, surface):
        try:
            surface.blit(self.image, (self.x, self.y))
        except AttributeError:
            pass

class BlueCoin(Coin): #bonus coin
    def __init__(self):
        Coin.__init__(self)
        self.image = bluecoin

class Bomb(Coin): #bomb
    def __init__(self):
        Coin.__init__(self)
        self.image = bomb

def coin_game():
    result = 0
    i = 1
    coinlist=[]
    gameclock = pygame.time.Clock()
    timer = 0
    cart = Cart()

    #set up texts
    time_text = basicFont.render('TIMER:',True, BLACK, WHITE)
    textbox = time_text.get_rect(center=(900, 170))
    points_text = basicFont.render('POINTS:',True, BLACK, WHITE)
    pointbox = points_text.get_rect(center=(100, 170))
    display_time = basicFont.render('0',True, BLACK, WHITE)
    timebox = display_time.get_rect(center=(900, 200))
    score = basicFont.render(str(cart.Points),True, BLACK, WHITE)
    scorebox = score.get_rect(center=(100, 200))

    while timer<=30:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        cart.handle_keys()
        windowSurface.blit(pygame.transform.scale(BG,(size)),(0, 0))
        cart.draw(windowSurface)

        #randomizing bonus coin/bomb/coin fall rate, can change this
        if i%3==0 or i%4==0:
            select = random.randint(1, 2)
            if select==1:
                C = BlueCoin()
            if select==2:
                C = Bomb()
        elif i%5==0 or i%7==0 or i&11==0:
            C = Bomb()
        else:
            C = Coin()
        coinlist.append(C)
        for B in coinlist[0:i:15]: #(use 14 or 15) this is for the rate at which objects fall, can change this
            B.draw(windowSurface)
            B.fall()
            cart.collect_item(B)
        pygame.display.flip()
        i+=1

        #update time
        seconds = gameclock.tick()/1000.0
        timer+=seconds
        int_timer = math.trunc(timer) #returns real value of timer to integer value
        if timer<30:
            display_time = basicFont.render(str(int_timer),True, BLACK, WHITE)
            windowSurface.blit(display_time, timebox)
        if timer>=30:
            time_text = basicFont.render('TIME UP!',True, BLACK, WHITE)
        windowSurface.blit(time_text, textbox)
        windowSurface.blit(points_text, pointbox)
        score = basicFont.render(str(cart.Points),True, BLACK, WHITE)
        windowSurface.blit(score, scorebox)
        pygame.display.flip()
    pygame.time.delay(500)
    pygame.quit()
    return

if __name__=='__main__':
    coin_game()
