from src.game_screens.screen import Screen
from src.misc.game_enums import Game_Mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.button import Button
from src.ui.text import Text
import pygame.key
import webbrowser

LEFT = 1


class Main_Menu_Screen(Screen):
    def __init__(self, pygame, res, surface, size):
        Screen.__init__(self, pygame, res, surface, size)

        self.texts['GameTitleShadow1'] = Text(
            pygame, res, surface, (self.center_x + 9, 100 + 9), 'Coin Fall', res.game_title_font, res.BLACK)

        self.texts['GameTitleShadow2'] = Text(
            pygame, res, surface, (self.center_x + 6, 100 + 6), 'Coin Fall', res.game_title_font, res.BLACK)
                    
        self.texts['GameTitleShadow3'] = Text(
            pygame, res, surface, (self.center_x + 3, 100 + 3), 'Coin Fall', res.game_title_font, res.BLACK)

        self.texts['GameTitle'] = Text(
            pygame, res, surface, (self.center_x, 100), 'Coin Fall', res.game_title_font, res.game_title_text_color)

        self.texts['Body1'] = Text(pygame, res, surface, (self.center_x, 190), 'Open-source coin collection game', 
            res.body_font, res.body_text_color)

        self.texts['Body2'] = Text(pygame, res, surface, (self.center_x, 220), 'Made with Python and Pygame', 
            res.body_font, res.body_text_color)

        self.buttons['Start'] = Button(
            pygame, res, surface, (self.center_x, 380), "Start")
        self.buttons['Tutorial'] = Button(
            pygame, res, surface, (self.center_x, 460), "Tutorial")
        self.buttons['Settings'] = Button(
            pygame, res, surface, (self.center_x, 540), "Settings")
        self.buttons['Credits'] = Button(
            pygame, res, surface, (self.center_x, 620), "Credits")
        self.buttons['Exit'] = Button(
            pygame, res, surface, (self.center_x, 700), "Exit")

    def update(self, events):
        self.surface.blit(self.res.EBG, (0, 0))

        for text in self.texts:
            self.texts[text].draw()

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP and x.button == LEFT), None)

        if mouseup_event is not None:
            if self.buttons['Start'].check_click(mouseup_event.pos):
                return Game_Mode.GAME_MODE

            if self.buttons['Tutorial'].check_click(mouseup_event.pos):
                return Game_Mode.TUTORIAL

            if self.buttons['Settings'].check_click(mouseup_event.pos):
                return Game_Mode.SETTINGS

            if self.buttons['Credits'].check_click(mouseup_event.pos):
                return Game_Mode.CREDITS

            if self.buttons['Exit'].check_click(mouseup_event.pos):
                return Game_Mode.QUIT

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.MAIN_MENU
