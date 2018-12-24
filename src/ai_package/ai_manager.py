#########################################
# AI Manager which acts as interface
# between the AI and the game
#########################################
from .ai_avoid_chase import AI_Avoid_Chase


class AI_Manager():

    def __init__(self):
        self.ai = AI_Avoid_Chase()

    def restart(self):
        self.ai.restart()

    def update(self, entity_list, cart):
        return self.ai.update(entity_list, cart)

    def game_over(self):
        self.ai.game_over()
