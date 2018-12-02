#############
# Blue Coin
############
from src.coin import Coin


class BlueCoin(Coin):  # bonus coin
    def __init__(self, res, size):
        Coin.__init__(self, res, size)
        self.image = res.bluecoin
