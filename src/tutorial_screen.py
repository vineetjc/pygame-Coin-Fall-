from src.screen import Screen
from src.game_enums import Game_mode
from pygame.locals import QUIT, KEYUP

class Tutorial_screen(Screen):
    def __init__(self, pygame, res, surface):
        Screen.__init__(self, pygame, res, surface)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def update(self, events):
        textsurface = self.font.render('Tutorial', False, (0, 0, 0))
        self.surface.fill(self.res.BGCOLOR)
        self.surface.blit(textsurface, (0, 0))
        
        
        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.TUTORIAL
