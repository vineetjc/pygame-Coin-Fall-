from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.text import Text
from src.ui.button import Button

LEFT = 1


class Game_Introduction_Screen(Screen):
    def __init__(self, pygame, res, surface, size, game_manager):
        Screen.__init__(self, pygame, res, surface, size)

        self.game_manager = game_manager

        self.texts['Heading1'] = Text(
            pygame, res, surface, (self.center_x + 3, 70 + 3), 'Introduction', res.heading1_font, res.BLACK)

        self.texts['Heading2'] = Text(
            pygame, res, surface, (self.center_x, 70), 'Introduction', res.heading1_font, res.game_title_text_color)

        self.texts['Body'] = Text(
            pygame, res, surface, (self.center_x, 130), 'How to play this game mode', res.body_font, res.body_text_color)

        self.buttons['Start'] = Button(
            pygame, res, surface, (self.center_x, 620), "Start")

        self.buttons['Back'] = Button(
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

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP and x.button == LEFT), None)

        if mouseup_event is not None:
            if self.buttons['Start'].check_click(mouseup_event.pos):
                return Game_mode.GAME

            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_mode.GAME_MODE

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.INTRODUCTION
