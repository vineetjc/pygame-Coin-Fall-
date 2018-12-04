################
# Bomb
################
from src.coin import Coin
from src.game_enums import Entity


class Bomb(Coin):
    def __init__(self, res, size, surface):
        Coin.__init__(self, res, size, surface)
        self.type = Entity.BOMB
        self.images = []
        self.image = res.bomb
