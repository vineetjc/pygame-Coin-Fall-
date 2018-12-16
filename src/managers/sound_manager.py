import pygame


class Play_sound:

    def __init__(self,background_music):
        self.background_music = pygame.mixer.music.load("res/Music/bg/background_music.mp3")

    def play_background_music(self):
        pygame.mixer.music.play(-1)
