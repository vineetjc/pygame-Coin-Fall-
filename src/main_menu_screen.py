from src.screen import Screen
from src.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.button import Button


class Main_menu_screen(Screen):
    def __init__(self, pygame, res, surface):
        Screen.__init__(self, pygame, res, surface)
        self.font = pygame.font.SysFont('cambria', 60)
        self.buttons['Game'] =      Button(pygame, res, surface, [20, 150, 300, 50], "Start Game")
        self.buttons['Tutorial'] =  Button(pygame, res, surface, [20, 220, 300, 50], "Tutorial")
        self.buttons['Settings'] =  Button(pygame, res, surface, [20, 290, 300, 50], "Settings")
        self.buttons['Exit'] =      Button(pygame, res, surface, [20, 360, 300, 50], "Exit")

    def update(self, events):
        textsurface = self.font.render('Main Menu', False, (0, 0, 0))
        self.surface.fill(self.res.BGCOLOR)
        self.surface.blit(textsurface, (20, 0))

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next((x for x in events if x.type == MOUSEBUTTONUP), None)

        if mouseup_event != None:
            if self.buttons['Game'].check_click(mouseup_event.pos):
                return Game_mode.MAIN_MENU

            if self.buttons['Tutorial'].check_click(mouseup_event.pos):
                return Game_mode.TUTORIAL

            if self.buttons['Settings'].check_click(mouseup_event.pos):
                return Game_mode.SETTINGS

            if self.buttons['Exit'].check_click(mouseup_event.pos):
                return Game_mode.QUIT

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.MAIN_MENU
