#############
# Blue Coin
############
from src.coin import Coin


class BlueCoin(Coin):  # bonus coin
    def __init__(self, res, size, surface):
        Coin.__init__(self, res, size, surface)
        self.image = res.bluecoin
        self.images = res.gold_coin_images
