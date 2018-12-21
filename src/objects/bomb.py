################
# Bomb
################
from src.objects.coin import Coin
from src.misc.game_enums import Entity
from src.animation_package import Animation


class Bomb(Coin):
    def __init__(self, res, size, surface):
        Coin.__init__(self, res, size, surface)
        self.type = Entity.BOMB
        self.animation = Animation(
            None, surface, res.bomb_anim, res.bomb_anim_size, 3, True)
