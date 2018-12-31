import os

from src.game_screens.screen import Screen
from src.misc.game_enums import Game_Mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.text import Text
from src.ui.button import Button

LEFT = 1


class Game_Over_Screen(Screen):
    def __init__(self, pygame, res, surface, size, game_manager):
        Screen.__init__(self, pygame, res, surface, size)
        self.game_manager = game_manager
        self.highscore_manager = self.game_manager.highscore_manager

        self.texts['Heading1'] = Text(
            pygame, res, surface, (self.center_x + 3, 70 + 3), 'Game Over', res.heading1_font, res.BLACK)

        self.texts['Heading2'] = Text(
            pygame, res, surface, (self.center_x, 70), 'Game Over', res.heading1_font, res.game_title_text_color)

        self.texts['Body'] = Text(
            pygame, res, surface, (self.center_x, 130), 'Game score and performance', res.body_font, res.body_text_color)

        self.texts['Game Mode'] = Text(
            pygame, res, surface, (self.center_x, 300), 'Game mode', res.heading3_font, res.heading3_text_color)

        self.texts['Score'] = Text(
            pygame, res, surface, (self.center_x, 380), 'Score: 0', res.body_font, res.body_text_color)

        self.texts['Highscore'] = Text(
            pygame, res, surface, (self.center_x, 420), 'Highscore: 0', res.body_font, res.body_text_color)

        self.buttons['Restart'] = Button(
            pygame, res, surface, (self.center_x, 620), "Restart")

        self.buttons['Back'] = Button(
            pygame, res, surface, (self.center_x, 700), "Back")

    def update(self, events):
        self.surface.blit(self.res.EBG, (0, 0))

        old_highscore = self.highscore_manager.data[self.game_manager.params['key']]
        new_score = self.game_manager.score

        if new_score > old_highscore:
            self.highscore_manager.data[self.game_manager.params['key']] = new_score
            self.highscore_manager.save_highscore_to_file()
            self.highscore_manager.load_highscore_from_file()

        for text in self.texts:
            self.texts[text].draw()

        for button in self.buttons:
            self.buttons[button].draw()

        self.texts['Game Mode'].change_text(
            self.game_manager.params['game_over_name'])

        self.texts['Score'].change_text('Score: ' + str(new_score))
        self.texts['Highscore'].change_text('Highscore: ' + str(old_highscore))

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP and x.button == LEFT), None)

        if mouseup_event is not None:
            if self.buttons['Restart'].check_click(mouseup_event.pos):
                return self.game_manager.params['game_mode']

            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_Mode.MAIN_MENU

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.GAME_OVER
