################
# Bomb
################
from src.coin import Coin


class Bomb(Coin):
    def __init__(self, res, size, surface):
        Coin.__init__(self, res, size, surface)
        self.images = []
        self.image = res.bomb
