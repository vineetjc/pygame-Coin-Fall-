from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.button import Button
from src.managers.game_manager import Game_manager  



class GameMode_screen(Screen):
    def __init__(self, pygame, res, surface):
        Screen.__init__(self, pygame, res, surface)
        self.font = pygame.font.SysFont('cambria', 60)
	self.game_manager=Game_manager()
        self.buttons['Easy'] =    Button(pygame, res, surface, [362, 150, 300, 50], "Easy")
        self.buttons['Medium'] =  Button(pygame, res, surface, [362, 220, 300, 50], "Medium")
        self.buttons['Hard'] =    Button(pygame, res, surface, [362, 290, 300, 50], "Hard")
	self.buttons['Back'] =    Button(pygame, res, surface, [362, 360, 300, 50], "Back")
        

    def update(self, events):
        textsurface = self.font.render('Select Difficulty:', True, self.res.WHITE)
        self.surface.blit(self.res.EBG,(0,0))
        self.surface.blit(textsurface, (362, 0))
              
        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next((x for x in events if x.type == MOUSEBUTTONUP), None)

        if mouseup_event != None:
            if self.buttons['Easy'].check_click(mouseup_event.pos):
		return self.game_manager.Difficulty["Easy"]
            
            if self.buttons['Medium'].check_click(mouseup_event.pos):
		return self.game_manager.Difficulty["Medium"]
            if self.buttons['Hard'].check_click(mouseup_event.pos):
		return self.game_manager.Difficulty["Hard"]
                        
            if self.buttons['Back'].check_click(mouseup_event.pos):
                return self.game_manager.Mode["Main_Menu"]

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return self.game_manager.Mode["QUIT"]

        return self.game_manager.Mode["GameMode"]
