##############################
# Define your input scheme,
# Buttons and axis' here
##############################

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
    input_list['horizontal'] = Axis('horizontal', {(pygame.K_a, pygame.K_d)})

    return input_list
