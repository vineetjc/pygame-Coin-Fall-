###############################################################
# Define your input scheme,
# Buttons and axis' here
#
# Guide for creating Buttons and Axis'
# Buttons:  first param is the name of the button, example:
#           reload, shoot etc.
#           second param is a list of pygame keycodes that
#           can be used for
#           that button, for example for reload, can use key
#           r or key 4
#           pressing key r or 4 will retun True
#           example use:
#           reload_game = input_manager.get_button('reload')
#
# Axis:     first param is the name of the Axis, example:
#           horizontal, vertical etc.
#           second param is a list of tuples. where the first
#           element of tuple is
#           the negative button and the second element is the
#           positive button.
#           for example, horizontal axis will have (key a, key d).
#           pressing key a will give -1, pressing key d will
#           give 1
#           example use:
#           move = input_manager.get_axis('horizontal')
##################################################################

from .input_button import Button
from .input_axis import Axis
import pygame.key


def get_input_list():
    input_list = dict()

    # reload
    input_list['reload'] = Button('reload', {pygame.K_r, pygame.K_4})

    # map
    input_list['map'] = Button('map', {pygame.K_m})

    # horizontal
    input_list['horizontal'] = Axis(
        'horizontal', {(pygame.K_a, pygame.K_d),
                       (pygame.K_LEFT, pygame.K_RIGHT)})

    input_list['horizontal_player1'] = Axis(
        'horizontal', {(pygame.K_a, pygame.K_d)})

    input_list['horizontal_player2'] = Axis(
        'horizontal', {(pygame.K_LEFT, pygame.K_RIGHT)})

    # vertical
    input_list['vertical'] = Axis(
        'vertical', {(pygame.K_s, pygame.K_w), (pygame.K_DOWN, pygame.K_UP)})

    # rotation
    input_list['rotation'] = Axis(
        'rotation', {(pygame.K_q, pygame.K_e)})

    # rotation2
    input_list['rotation2'] = Axis(
        'rotation2', {(pygame.K_o, pygame.K_l)})

    # rotation3
    input_list['rotation3'] = Axis(
        'rotation3', {(pygame.K_i, pygame.K_k)})

    # rotation4
    input_list['rotation4'] = Axis(
        'rotation4', {(pygame.K_u, pygame.K_j)})

    return input_list
