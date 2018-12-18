

class Text():
    def __init__(self, pygame, res, surface, pos, text, font, color, alignment='center'):
        self.pygame = pygame
        self.res = res
        self.surface = surface
        self.pos = pos
        self.text = text
        self.font = font
        self.color = color
        self.text_render = self.font.render(text, True, color)
        self.alignment = alignment
        self.set_alignment(self.alignment)

    def draw(self):
        self.surface.blit(self.text_render, self.rect)

    def change_text(self, text):
        self.text_render = self.font.render(text, True, self.color)
        self.set_alignment(self.alignment)

    def change_pos(self, pos):
        self.set_alignment(self.alignment)

    def set_alignment(self, alignment):
        if alignment is 'center':
            self.rect = self.text_render.get_rect(center=self.pos)
        elif alignment is 'right':
            self.rect = self.text_render.get_rect(midright=self.pos)
        elif alignment is 'left':
            self.rect = self.text_render.get_rect(midleft=self.pos)
