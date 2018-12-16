from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode, Difficulty
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.button import Button


class Game_Mode_Screen(Screen):
    def __init__(self, pygame, res, surface, size, game_manager):
        Screen.__init__(self, pygame, res, surface, size)
        self.game_manager = game_manager
        
        self.buttons['Classic'] =   Button(pygame, res, surface, (self.center_x, 170), "Classic")
        self.buttons['Infinite'] =  Button(pygame, res, surface, (self.center_x, 240), "Infinite")
        self.buttons['1v1'] =       Button(pygame, res, surface, (self.center_x, 310), "1 vs 1")

        self.buttons['Easy'] =      Button(pygame, res, surface, (20, 520), "Easy")
        self.buttons['Medium'] =    Button(pygame, res, surface, (240, 520), "Medium")
        self.buttons['Hard'] =      Button(pygame, res, surface, (460, 520), "Hard")

        self.buttons['Back'] =      Button(pygame, res, surface, (self.center_x, 700), "Back")

    def update(self, events):
        textsurface = self.res.heading1_font.render('Select Game Mode:', True, self.res.WHITE)
        textsurface2 = self.res.heading3_font.render('Select Mode:', True, self.res.WHITE)
        textsurface3 = self.res.heading3_font.render('Select Difficulty:', True, self.res.WHITE)
        self.surface.blit(self.res.EBG, (0, 0))
        self.surface.blit(textsurface, (20, 0))
        self.surface.blit(textsurface2, (20, 100))
        self.surface.blit(textsurface3, (20, 450))

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP), None)

        if mouseup_event is not None:
            if self.buttons['Easy'].check_click(mouseup_event.pos):
                self.game_manager.difficulty = Difficulty.EASY
                return Game_mode.GAME

            if self.buttons['Medium'].check_click(mouseup_event.pos):
                self.game_manager.difficulty = Difficulty.MEDIUM
                return Game_mode.GAME

            if self.buttons['Hard'].check_click(mouseup_event.pos):
                self.game_manager.difficulty = Difficulty.HARD
                return Game_mode.GAME

            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_mode.MAIN_MENU

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.GAME_MODE
