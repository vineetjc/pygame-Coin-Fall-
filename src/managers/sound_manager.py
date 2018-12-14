import pygame



class Play_sound:


	def init(self,background_music,coin_pickup):
		self.background_music = pygame.mixer.music.load("res/Music/bg/background_music.wav")
		self.coin_pickup = pygame.mixer.Sound("res/Music/effects/coin_pickup.wav")

	def play_music(self,background_music):
		self.background_music = pygame.mixer.music.play(-1)
	

	def stop_music(self,background_music):
		self.background_music = pygame.mixer.music.stop()
	

	def play_effect(self,coin_pickup):
		self.coin_pickup = pygame.mixer.Sound.play()
