import webbrowser

from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.text import Text
from src.ui.button import Button

LEFT = 1


class Credits_screen(Screen):
    def __init__(self, pygame, res, surface, size):
        Screen.__init__(self, pygame, res, surface, size)
        self.buttons['Vineet'] = Button(
            pygame, res, surface, (self.center_x, 150), "Vineet")
        self.buttons['Amrit'] = Button(
            pygame, res, surface, (self.center_x, 220), "Amrit")
        self.buttons['Venturillo'] = Button(
            pygame, res, surface, (self.center_x, 290), "Venturillo")
        self.buttons['Divyang'] = Button(
            pygame, res, surface, (self.center_x, 360), "Divyang")
        self.buttons['Azmal'] = Button(
            pygame, res, surface, (self.center_x, 430), "Azmal")
        self.buttons['Abhinandan'] = Button(
            pygame, res, surface, (self.center_x, 500), "Abhinandan")
        self.buttons['Back'] = Button(
            pygame, res, surface, (self.center_x, 700), "Back")

    def update(self, events):
        textsurface = self.res.heading1_font.render('Credits', True, self.res.WHITE)
        textsurface2 = self.res.body_font.render(
            'People who have contributed to this project.', True, self.res.WHITE)
        self.surface.blit(self.res.EBG, (0, 0))
        self.surface.blit(textsurface, (20, 0))
        self.surface.blit(textsurface2, (20, 100))

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP and x.button == LEFT), None)

        if mouseup_event is not None:
            if self.buttons['Vineet'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/vineetjc')
                return Game_mode.CREDITS

            if self.buttons['Amrit'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/amrit-choudhary')
                return Game_mode.CREDITS

            if self.buttons['Venturillo'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/SeraphWedd')
                return Game_mode.CREDITS

            if self.buttons['Divyang'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/divyang-mittal')
                return Game_mode.CREDITS

            if self.buttons['Azmal'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/MD-AZMAL')
                return Game_mode.CREDITS

            if self.buttons['Abhinandan'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/kainthcool')
                return Game_mode.CREDITS

            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_mode.MAIN_MENU

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.CREDITS
