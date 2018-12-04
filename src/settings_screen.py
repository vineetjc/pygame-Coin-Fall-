from src.screen import Screen
from src.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.button import Button


class Settings_screen(Screen):
    def __init__(self, pygame, res, surface):
        Screen.__init__(self, pygame, res, surface)
        self.font = pygame.font.SysFont('cambria', 60)
        self.font2 = pygame.font.SysFont('cambria', 30)
        self.buttons['Back'] =  Button(pygame, res, surface, [20, 360, 300, 50], "Back")

    def update(self, events):
        textsurface = self.font.render('Settings', True, (0, 0, 0))
        textsurface2 = self.font2.render('This is the settings menu.', True, (0, 0, 0))
        self.surface.fill(self.res.BGCOLOR)
        self.surface.blit(textsurface, (20, 0))
        self.surface.blit(textsurface2, (20, 100))

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next((x for x in events if x.type == MOUSEBUTTONUP), None)

        if mouseup_event != None:
            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_mode.MAIN_MENU

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.SETTINGS
