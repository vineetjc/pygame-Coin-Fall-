

class Image():
    def __init__(self, pygame, res, surface, pos, image):
        self.pygame = pygame
        self.res = res
        self.surface = surface
        temp_rect = pygame.Rect((0, 0), (0, 0))
        temp_rect.center = pos
        self.rect = temp_rect.center
        self.image = image

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def change_image(self, image):
        slf.image = image

    def change_pos(self, pos):
        temp_rect = pygame.Rect((0, 0), (0, 0))
        temp_rect.center = pos
        self.rect = pos
