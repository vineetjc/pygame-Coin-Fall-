################
# Bomb
################
from src.coin import Coin


class Bomb(Coin):
    def __init__(self, res, size):
        Coin.__init__(self, res, size)
        self.images = []
        self.image = res.bomb
