######################################
# Example AI which moves based on
# the lowest bomb location and also
# chases coins when it's safe
#######################################
import math
from .ai_base import AI_Base
from src.misc.game_enums import Entity


class AI_Avoid_Chase(AI_Base):

    def __init__(self):
        pass

    def restart(self):
        pass

    def update(self, entity_list, cart):
        cart_x = cart.get_center()[0]
        entity_list_copy = entity_list.copy()

        bombs_list = [x for x in entity_list_copy if (
            x.type is Entity.BOMB) and (x.y < 700) and (x.y > 300)]

        coins_list = [x for x in entity_list_copy if (
            (x.type is Entity.COIN) or (x.type is Entity.BLUE_COIN)) and (x.y < 600)]

        if len(bombs_list) > 0:
            lowest_bomb_x = bombs_list[0].x
        else:
            lowest_bomb_x = cart_x

        if len(coins_list) > 0:
            lowest_coin_x = coins_list[0].x
        else:
            lowest_coin_x = cart_x

        delta_bomb = lowest_bomb_x - cart_x
        delta_coin = lowest_coin_x - cart_x

        if (abs(delta_bomb) > 150) or (len(bombs_list) == 0):    # is safe from bomb

            if abs(delta_coin) < 20:
                ai_movement = 0
            else:
                if delta_coin > 0:
                    ai_movement = 1
                else:
                    ai_movement = -1

        else:                                                   # not safe from bomb
            if delta_bomb > 0:
                ai_movement = -1
            else:
                ai_movement = 1

        return ai_movement
