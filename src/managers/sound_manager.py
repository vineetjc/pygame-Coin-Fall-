##########################################
# manages sounds
###########################################

import pygame


class Play_sound:

    #set up background music
    def __init__(self,background_music):
        self.background_music = pygame.mixer.music.load("res/Music/bg/background_music.mp3")

    #plays on loop
    def play_background_music(self):
        pygame.mixer.music.play(-1)
