#############
# Blue Coin
############
from src.coin import Coin
from src.game_enums import Entity


class BlueCoin(Coin):  # bonus coin
    def __init__(self, res, size, surface):
        Coin.__init__(self, res, size, surface)
        self.type = Entity.BLUE_COIN
        self.image = res.bluecoin
        self.images = res.gold_coin_images
