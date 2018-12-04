

class Button():
    def __init__(self, pygame, res, surface, rect, text):
        self.pygame = pygame
        self.res = res
        self.surface = surface
        self.rect = self.pygame.Rect(rect)
        self.text = text
        self.font = pygame.font.SysFont('cambria', 40)

    def draw(self):
        self.pygame.draw.rect(self.surface, self.res.BUTTONCOLOR, self.rect)
        textsurface = self.font.render(self.text, True, self.res.WHITE)
        self.surface.blit(textsurface, self.rect)

    def check_click(self, pos):
        return self.rect.collidepoint(pos)
