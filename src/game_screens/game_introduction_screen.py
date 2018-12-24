from src.game_screens.screen import Screen
from src.misc.game_enums import Game_Mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.text import Text
from src.ui.button import Button
from src.managers.gameplay_parameters import Gameplay_Parameters

LEFT = 1


class Game_Introduction_Screen(Screen):
    def __init__(self, pygame, res, surface, size, game_manager):
        Screen.__init__(self, pygame, res, surface, size)

        self.game_manager = game_manager
        self.params_list = Gameplay_Parameters().params_list

        self.texts['Heading1'] = Text(
            pygame, res, surface, (self.center_x + 3, 70 + 3), 'Introduction', res.heading1_font, res.BLACK)

        self.texts['Heading2'] = Text(
            pygame, res, surface, (self.center_x, 70), 'Introduction', res.heading1_font, res.game_title_text_color)

        self.texts['Body'] = Text(
            pygame, res, surface, (self.center_x, 130), 'How to play this game mode', res.body_font, res.body_text_color)

        self.buttons_classic = {}
        self.buttons_others = {}

        self.buttons_classic['Easy'] = Button(
            pygame, res, surface, (self.center_x - 250, 620), "Easy")

        self.buttons_classic['Medium'] = Button(
            pygame, res, surface, (self.center_x + 000, 620), "Medium")

        self.buttons_classic['Hard'] = Button(
            pygame, res, surface, (self.center_x + 250, 620), "Hard")

        self.buttons_others['Start'] = Button(
            pygame, res, surface, (self.center_x, 620), "Start")

        self.buttons_classic['Back'] = Button(
            pygame, res, surface, (self.center_x, 700), "Back")

        self.buttons_others['Back'] = Button(
            pygame, res, surface, (self.center_x, 700), "Back")

    def update(self, events):
        self.surface.blit(self.res.EBG, (0, 0))

        self.texts['Heading1'].change_text(
            self.game_manager.params['display_name'])
        self.texts['Heading2'].change_text(
            self.game_manager.params['display_name'])
        self.texts['Body'].change_text(
            self.game_manager.params['introduction'])

        for text in self.texts:
            self.texts[text].draw()

        if self.game_manager.params['display_name'] is self.params_list['classic_medium']['display_name']:
            for button in self.buttons_classic:
                self.buttons_classic[button].draw()
        else:
            for button in self.buttons_others:
                self.buttons_others[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP and x.button == LEFT), None)

        if mouseup_event is not None:

            if self.game_manager.params['display_name'] is self.params_list['classic_medium']['display_name']:

                if self.buttons_classic['Easy'].check_click(mouseup_event.pos):
                    self.game_manager.params = self.params_list['classic_easy']
                    return self.game_manager.params['game_mode']

                if self.buttons_classic['Medium'].check_click(mouseup_event.pos):
                    self.game_manager.params = self.params_list['classic_medium']
                    return self.game_manager.params['game_mode']

                if self.buttons_classic['Hard'].check_click(mouseup_event.pos):
                    self.game_manager.params = self.params_list['classic_hard']
                    return self.game_manager.params['game_mode']

                if self.buttons_classic['Back'].check_click(mouseup_event.pos):
                    return Game_Mode.GAME_MODE

            else:
                if self.buttons_others['Start'].check_click(mouseup_event.pos):
                    return self.game_manager.params['game_mode']

                if self.buttons_others['Back'].check_click(mouseup_event.pos):
                    return Game_Mode.GAME_MODE

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.INTRODUCTION
