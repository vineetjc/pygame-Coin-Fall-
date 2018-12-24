from src.game_screens.screen import Screen
from src.misc.game_enums import Game_Mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.text import Text
from src.ui.button import Button
from src.managers.gameplay_parameters import Gameplay_Parameters

LEFT = 1


class Game_Mode_Screen(Screen):
    def __init__(self, pygame, res, surface, size, game_manager):
        Screen.__init__(self, pygame, res, surface, size)
        self.game_manager = game_manager
        self.params_list = Gameplay_Parameters().params_list

        self.texts['Heading1'] = Text(
            pygame, res, surface, (self.center_x + 3, 70 + 3), 'Select Game Mode', res.heading1_font, res.BLACK)

        self.texts['Heading2'] = Text(
            pygame, res, surface, (self.center_x, 70), 'Select Game Mode', res.heading1_font, res.game_title_text_color)

        self.texts['Body'] = Text(
            pygame, res, surface, (self.center_x, 130), 'Choose your game mode', res.body_font, res.body_text_color)

        self.texts['Game Mode'] = Text(
            pygame, res, surface, (self.center_x, 240), 'Game mode', res.heading3_font, res.heading3_text_color)

        self.buttons['Classic'] = Button(
            pygame, res, surface, (self.center_x - 250, 320), "Classic")
        self.buttons['Infinite'] = Button(
            pygame, res, surface, (self.center_x + 000, 320), "Infinite")
        self.buttons['1v1'] = Button(
            pygame, res, surface, (self.center_x + 250, 320), "1 vs 1")

        self.buttons['AI'] = Button(
            pygame, res, surface, (self.center_x - 250, 400), "AI")
        self.buttons['Hardcore'] = Button(
            pygame, res, surface, (self.center_x + 000, 400), "Hardcore")
        self.buttons['Heist'] = Button(
            pygame, res, surface, (self.center_x + 250, 400), "Heist")

        self.buttons['Back'] = Button(
            pygame, res, surface, (self.center_x, 700), "Back")

    def update(self, events):
        self.surface.blit(self.res.EBG, (0, 0))

        for text in self.texts:
            self.texts[text].draw()

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP and x.button == LEFT), None)

        if mouseup_event is not None:
            if self.buttons['Classic'].check_click(mouseup_event.pos):
                self.game_manager.params = self.params_list['classic_medium']
                return Game_Mode.INTRODUCTION

            if self.buttons['Infinite'].check_click(mouseup_event.pos):
                self.game_manager.params = self.params_list['infinite']
                return Game_Mode.INTRODUCTION

            if self.buttons['1v1'].check_click(mouseup_event.pos):
                self.game_manager.params = self.params_list['1v1']
                return Game_Mode.INTRODUCTION

            if self.buttons['AI'].check_click(mouseup_event.pos):
                self.game_manager.params = self.params_list['ai']
                return Game_Mode.INTRODUCTION

            if self.buttons['Hardcore'].check_click(mouseup_event.pos):
                self.game_manager.params = self.params_list['hardcore']
                return Game_Mode.INTRODUCTION

            if self.buttons['Heist'].check_click(mouseup_event.pos):
                self.game_manager.params = self.params_list['heist']
                return Game_Mode.INTRODUCTION

            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_Mode.MAIN_MENU

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.GAME_MODE
