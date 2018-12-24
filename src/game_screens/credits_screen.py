import webbrowser

from src.game_screens.screen import Screen
from src.misc.game_enums import Game_Mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.text import Text
from src.ui.button import Button

LEFT = 1


class Credits_Screen(Screen):
    def __init__(self, pygame, res, surface, size):
        Screen.__init__(self, pygame, res, surface, size)

        self.texts['Heading1'] = Text(
            pygame, res, surface, (self.center_x + 3, 70 + 3), 'Credits', res.heading1_font, res.BLACK)

        self.texts['Heading2'] = Text(
            pygame, res, surface, (self.center_x, 70), 'Credits', res.heading1_font, res.game_title_text_color)

        self.texts['Body'] = Text(
            pygame, res, surface, (self.center_x, 130), 'People who have contributed to this project', res.body_font, res.body_text_color)

        self.buttons['Contribute'] = Button(
            pygame, res, surface, (self.center_x, 200), "Contribute")
        self.buttons['Vineet'] = Button(
            pygame, res, surface, (self.center_x - 150, 300), "Vineet")
        self.buttons['Amrit'] = Button(
            pygame, res, surface, (self.center_x + 150, 300), "Amrit")
        self.buttons['Kartik'] = Button(
            pygame, res, surface, (self.center_x - 150, 380), "Kartik")
        self.buttons['Venturillo'] = Button(
            pygame, res, surface, (self.center_x + 150, 380), "Venturillo")
        self.buttons['Shikhar'] = Button(
            pygame, res, surface, (self.center_x - 150, 460), "Shikhar")
        self.buttons['Divyang'] = Button(
            pygame, res, surface, (self.center_x + 150, 460), "Divyang")
        self.buttons['Azmal'] = Button(
            pygame, res, surface, (self.center_x - 150, 540), "Azmal")
        self.buttons['Abhinandan'] = Button(
            pygame, res, surface, (self.center_x + 150, 540), "Abhinandan")
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
            if self.buttons['Contribute'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/vineetjc/pygame-Coin-Fall-')
                return Game_Mode.CREDITS

            if self.buttons['Vineet'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/vineetjc')
                return Game_Mode.CREDITS

            if self.buttons['Amrit'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/amrit-choudhary')
                return Game_Mode.CREDITS

            if self.buttons['Kartik'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/kartikct25')
                return Game_Mode.CREDITS

            if self.buttons['Venturillo'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/SeraphWedd')
                return Game_Mode.CREDITS

            if self.buttons['Shikhar'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/johri002')
                return Game_Mode.CREDITS

            if self.buttons['Divyang'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/divyang-mittal')
                return Game_Mode.CREDITS

            if self.buttons['Azmal'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/MD-AZMAL')
                return Game_Mode.CREDITS
            
            if self.buttons['Abhinandan'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/kainthcool')
                return Game_Mode.CREDITS
            
            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_Mode.MAIN_MENU

        for event in events:
            if event.type == QUIT:
                return Game_Mode.QUIT

        return Game_Mode.CREDITS
