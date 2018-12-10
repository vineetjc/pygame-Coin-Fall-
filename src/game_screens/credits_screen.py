import webbrowser

from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.button import Button


class Credits_screen(Screen):
    def __init__(self, pygame, res, surface):
        Screen.__init__(self, pygame, res, surface)
        self.font = pygame.font.SysFont('cambria', 60)
        self.font2 = pygame.font.SysFont('cambria', 30)
        self.buttons['Vineet'] =        Button(pygame, res, surface, [20, 150, 300, 50], "Vineet")
        self.buttons['Amrit'] =         Button(pygame, res, surface, [20, 220, 300, 50], "Amrit")
        self.buttons['Venturillo'] =    Button(pygame, res, surface, [20, 290, 300, 50], "Venturillo")
        self.buttons['Divyang'] =       Button(pygame, res, surface, [20, 360, 300, 50], "Divyang")
        self.buttons['Azmal'] =         Button(pygame, res, surface, [20, 430, 300, 50], "Azmal")
        self.buttons['Abhinandan'] =    Button(pygame, res, surface, [20, 500, 300, 50], "Abhinandan")
        self.buttons['Gitter'] =        Button(pygame, res, surface, [20, 570, 300, 50], "Gitter")
        self.buttons['Back'] =          Button(pygame, res, surface, [20, 640, 300, 50], "Back")

    def update(self, events):
        textsurface = self.font.render('Credits', True, self.res.WHITE)
        textsurface2 = self.font2.render('People who have contributed to this project.', True, self.res.WHITE)
        self.surface.blit(self.res.EBG,(0,0))
        self.surface.blit(textsurface, (20, 0))
        self.surface.blit(textsurface2, (20, 100))
              
        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next((x for x in events if x.type == MOUSEBUTTONUP), None)

        if mouseup_event != None:
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

            if self.buttons['Gitter'].check_click(mouseup_event.pos):
                webbrowser.open_new_tab('https://github.com/gitter-badger')
                return Game_mode.CREDITS
                        
            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_mode.MAIN_MENU

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.CREDITS