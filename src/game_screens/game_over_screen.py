import os
import pygame
import time

from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.text import Text
from src.ui.button import Button

LEFT = 1


class Game_over_screen(Screen):
    def __init__(self, pygame, res, surface, size, game_manager):
        Screen.__init__(self, pygame, res, surface, size)
        self.game_manager = game_manager
        self.exploded = False

        self.texts['Heading1'] = Text(
            pygame, res, surface, (self.center_x + 3, 70 + 3), 'Game Over', res.heading1_font, res.BLACK)

        self.texts['Heading2'] = Text(
            pygame, res, surface, (self.center_x, 70), 'Game Over', res.heading1_font, res.game_title_text_color)
        
        self.texts['Body'] = Text(
            pygame, res, surface, (self.center_x, 130), 'Game score and performance', res.body_font, res.body_text_color)


        self.buttons['Restart'] = Button(
            pygame, res, surface, (self.center_x, 290), "Restart")
        self.buttons['Back'] = Button(
            pygame, res, surface, (self.center_x, 700), "Back")

    def update(self, events):
        if not self.exploded:
            expl = pygame.image.load('res/images/misc/explosion.png')
            self.surface.blit(expl , (100,500))
            self.pygame.display.update()
            time.sleep(2)
            self.exploded = True
        if not os.path.isfile("highscore.txt"):
            with open("highscore.txt", "w") as hiscore_file:
                hiscore_file.write("0")
        hisc = open("highscore.txt", "r")
        highscore = hisc.read()
        maxscore = max(int(highscore), int(self.game_manager.score))
        if int(highscore) < int(self.game_manager.score):
            hisc.close()
            hisc = open("highscore.txt", "w")
            hisc.write(str(self.game_manager.score))
        hisc.close()

        textsurface2 = self.res.body_font.render(
            'Score: ' + str(self.game_manager.score), True, self.res.WHITE)

        textsurface3 = self.res.body_font.render(
            'Highscore: ' + str(maxscore), True, self.res.WHITE)
        self.surface.blit(self.res.EBG, (0, 0))
        self.surface.blit(textsurface2, (20, 100))
        self.surface.blit(textsurface3, (20, 150))

        for text in self.texts:
            self.texts[text].draw()

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP and x.button == LEFT), None)

        if mouseup_event is not None:
            if self.buttons['Restart'].check_click(mouseup_event.pos):
                return Game_mode.GAME_MODE

            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_mode.MAIN_MENU

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.GAME_OVER
