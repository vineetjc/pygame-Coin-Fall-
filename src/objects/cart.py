##################
# Cart Class
##################
import math
from src.misc.game_enums import Entity
import pygame


class Cart(object):
    def __init__(self, res, size, surface, game_manager):
        self.type = Entity.CART
        self.res = res
        self.size = size
        self.surface = surface
        self.game_manager = game_manager
        self.input = game_manager.input
        self.animation_manager = game_manager.animation_manager
        self.image = res.cart_img
        self.x = (size[0] / 2) - 80
        self.y = size[1] - 120
        self.dead = False  # Add this for game end check
        self.speed = 10

    def move(self):
        movement = self.input.get_axis('horizontal') * self.speed
        desired_movement = self.x + movement
        final_movement = max(min(desired_movement, self.size[0] - 140), -10)
        self.x = final_movement

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

    def collision_rect(self):
        temp_rect = pygame.Rect(0, 0, 100, 30)
        cart_image_rect = pygame.Rect(self.x, self.y, 160, 134)
        temp_rect.midtop = (
            cart_image_rect.midtop[0], cart_image_rect.midtop[1] + 20)
        return temp_rect

    def get_center(self):
        cart_image_rect = pygame.Rect(self.x, self.y, 160, 134)
        return cart_image_rect.center

    def check_collision(self, coin):
        return self.collision_rect().colliderect(coin.collision_rect())
