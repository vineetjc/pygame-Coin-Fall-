################
# Coin class
################
import random
from src.misc.game_enums import Entity
from src.animation_package import Animation
import pygame


class Coin():
    def __init__(self, res, size, surface, spawn_x, spawn_y):
        self.type = Entity.COIN
        self.surface = surface
        self.animation = Animation(
            None, surface, res.silver_coin_anim, res.silver_coin_anim_size, 3, True)
        self.x = spawn_x
        self.y = spawn_y
        self.anim_index = 0
        self.anim_counter = 0
        self.anim_tick_length = 4
        self.collected = False
        self.collision_size = res.silver_coin_anim_size

    def fall(self):
        self.y += 7

    def draw(self):
        if self.collected:
            return

        self.animation.draw((self.x, self.y))

    def advance_animation(self):
        self.anim_counter += 1

        if self.anim_counter > self.anim_tick_length:
            self.anim_counter = 0
            self.anim_index += 1

            if self.anim_index >= len(self.images):
                self.anim_index = 0

    def collect(self):
        self.collected = True

    def collision_rect(self):
        rect = pygame.Rect(0, 0, self.collision_size, self.collision_size)
        rect.center = (self.x, self.y)
        return rect
