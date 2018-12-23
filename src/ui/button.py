

class Button():
    def __init__(self, pygame, res, surface, pos, text):
        self.pygame = pygame
        self.res = res
        self.surface = surface
        temp_rect = self.pygame.Rect(pos, self.res.button_image_size)
        temp_rect.center = pos
        self.rect = temp_rect
        self.text = text
        self.font = res.button_font2
        self.text_render = self.font.render(text, True, res.button_text_color)
        self.text_rect = self.text_render.get_rect(center=self.rect.center)

    def draw(self):
        self.surface.blit(self.res.button_image, self.rect.topleft)
        self.surface.blit(self.text_render, self.text_rect)

    def check_click(self, pos):
        return self.rect.collidepoint(pos)
