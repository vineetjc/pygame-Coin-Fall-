####################################
# Example AI which moves based on
# the lowest bomb location
####################################
import math
from .ai_base import AI_Base
from src.misc.game_enums import Entity


class AI_Avoid_Bomb(AI_Base):

    def __init__(self):
        pass

    def restart(self):
        pass

    def update(self, entity_list, cart):
        cart_x = cart.get_center()[0]
        entity_list_copy = entity_list.copy()
        bombs_list = [x for x in entity_list_copy if (
            x.type is Entity.BOMB) and (x.y < 600)]

        if len(bombs_list) > 0:
            lowest_bomb_x = bombs_list[0].x
        else:
            lowest_bomb_x = cart_x

        delta = lowest_bomb_x - cart_x

        if abs(delta) > 150:
            ai_movement = 0
        else:
            if delta > 0:
                ai_movement = -1
            else:
                ai_movement = 1

        if len(bombs_list) == 0:
            ai_movement = 0

        return ai_movement
