from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.button import Button
from src.ui.text import Text
import pygame.key
import webbrowser

LEFT = 1


class Main_menu_screen(Screen):
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

        self.texts['Body1'] = Text(pygame, res, surface, (self.center_x, 190), 'Open source coin collection game', 
            res.body_font, res.body_text_color)

        self.texts['Body2'] = Text(pygame, res, surface, (self.center_x, 220), 'Made with Python and Pygame', 
            res.body_font, res.body_text_color)

        self.buttons['Start'] = Button(
            pygame, res, surface, (self.center_x, 300), "Start")
        self.buttons['Tutorial'] = Button(
            pygame, res, surface, (self.center_x, 380), "Tutorial")
        self.buttons['Settings'] = Button(
            pygame, res, surface, (self.center_x, 460), "Settings")
        self.buttons['Credits'] = Button(
            pygame, res, surface, (self.center_x, 540), "Credits")
        self.buttons['Contribute'] = Button(
            pygame, res, surface, (self.center_x, 620), "Contribute")
        self.buttons['Exit'] = Button(
            pygame, res, surface, (self.center_x, 700), "Exit")

    def update(self, events):
        self.surface.blit(self.res.EBG, (0, 0))

        for text in self.texts:
            self.texts[text].draw()

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP), None)

        if mouseup_event is not None:
            if self.buttons['Start'].check_click(mouseup_event.pos):
                return Game_mode.GAME_MODE

            if self.buttons['Tutorial'].check_click(mouseup_event.pos):
                return Game_mode.TUTORIAL

            if self.buttons['Settings'].check_click(mouseup_event.pos):
                return Game_mode.SETTINGS

            if self.buttons['Credits'].check_click(mouseup_event.pos):
                return Game_mode.CREDITS

            if self.buttons['Contribute'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab(
                    'https://github.com/vineetjc/pygame-Coin-Fall-')
                return Game_mode.MAIN_MENU

            if self.buttons['Exit'].check_click(mouseup_event.pos):
                return Game_mode.QUIT

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.MAIN_MENU
