#############
# Blue Coin
############
from src.objects.coin import Coin
from src.misc.game_enums import Entity
from src.animation_package import Animation


class BlueCoin(Coin):  # bonus coin
    def __init__(self, res, size, surface, spawn_x, spawn_y):
        Coin.__init__(self, res, size, surface, spawn_x, spawn_y)
        self.type = Entity.BLUE_COIN
        self.animation = Animation(
            None, surface, res.gold_coin_anim, res.gold_coin_anim_size, 3, True)
