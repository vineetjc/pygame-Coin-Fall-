from src.game_screens.screen import Screen
from src.misc.game_enums import Game_Mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.text import Text
from src.ui.button import Button

LEFT = 1


class Settings_Screen(Screen):
    def __init__(self, pygame, res, surface, size, game_manager):
        Screen.__init__(self, pygame, res, surface, size)
        self.highscore_manager = game_manager.highscore_manager

        self.texts['Heading1'] = Text(
            pygame, res, surface, (self.center_x + 3, 70 + 3), 'Settings', res.heading1_font, res.BLACK)

        self.texts['Heading2'] = Text(
            pygame, res, surface, (self.center_x, 70), 'Settings', res.heading1_font, res.game_title_text_color)

        self.texts['Body'] = Text(
            pygame, res, surface, (self.center_x, 130), 'Edit game settings here', res.body_font, res.body_text_color)

        self.buttons['Reset'] = Button(
            pygame, res, surface, (self.center_x, 380), "Reset")

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
            if self.buttons['Reset'].check_click(mouseup_event.pos):
                self.highscore_manager.reset_highscore()
                return Game_Mode.MAIN_MENU

            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_Mode.MAIN_MENU

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.SETTINGS
