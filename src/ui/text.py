

class Text():
    def __init__(self, pygame, res, surface, pos, text, font, color):
        self.pygame = pygame
        self.res = res
        self.surface = surface
        self.pos = pos
        self.text = text
        self.font = font
        self.color = color
        self.text_render = self.font.render(text, True, color)
        self.rect = self.text_render.get_rect(center=pos)

    def draw(self):
        self.surface.blit(self.text_render, self.rect)

    def change_text(self, text):
        self.text_render = self.font.render(text, True, self.color)
        self.rect = self.text_render.get_rect(center=self.pos)

    def change_pos(self, pos):
        self.rect = self.text_render.get_rect(center=pos)

    def check_click(self, pos):
        return self.rect.collidepoint(pos)
