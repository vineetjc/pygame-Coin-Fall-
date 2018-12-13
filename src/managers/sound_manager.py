class play_sound:


	def init(self):
		self.background_music = pygame.mixer.music.load("res/Music/background_music.mp3")
	

	def play_music(self):
		self.background_music = pygame.mixer.music.play(-1)
