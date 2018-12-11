##########################################################
# game manager
# will have global game variables like score and settings
##########################################################

class Game_manager(object):
    def __init__(self):
        self.score = 0
        self.time = 0
	self.Difficulty = {"Easy":25,"Medium":15,"Hard":5}    
        self.Mode = {"GameMode":0,"Main_Menu":1,"QUIT":-1}
    
    def reset(self):
        self.score = 0
        self.time = 0
	
        
