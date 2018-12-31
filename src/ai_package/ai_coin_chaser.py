####################################
# Example AI which moves based on
# the lowest coin location
####################################
import math
from .ai_base import AI_Base
from src.misc.game_enums import Entity


class AI_Coin_Chaser(AI_Base):

    def __init__(self):
        pass

    def restart(self):
        pass

    def update(self, entity_list, cart):
        cart_x = cart.get_center()[0]
        entity_list_copy = entity_list.copy()
        coins_list = [x for x in entity_list_copy if (
            x.type is Entity.COIN) or (x.type is Entity.BLUE_COIN)]

        if len(coins_list) > 0:
            lowest_coin_x = coins_list[0].x
        else:
            lowest_coin_x = cart_x

        delta = lowest_coin_x - cart_x

        if abs(delta) < 20:
            ai_movement = 0
        else:
            if delta > 0:
                ai_movement = 1
            else:
                ai_movement = -1

        return ai_movement
