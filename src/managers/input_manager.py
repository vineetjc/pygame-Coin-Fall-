##########################################
# Manages input
# Will act as a wrapper around the pygame input functionality
# and provide ease of use for common input tasks
# Will support:
#   multiple keys for same action
#   axis input (three possible input: -1, 0, 1)
#   joystick input
###########################################

from src.ui.input_button import Button
from src.ui.input_axis import Axis
import pygame.key


class Input_Manager():
    ''' Will have the states of all the buttons and axis defined by the game.
        These states can be retrieved from here with simple functions
        Will get these states at the start of the frame
    '''

    def __init__(self):
        self.input_list = self.get_input_list()
        print (self.input_list)

    def update(self, events):
        pass

    def get_button(self, button_name):
        pass

    def get_axis(self, axis_name):
        pass

    # define all the buttons here
    def get_input_list(self):
        input_list = dict()

        # reload
        input_list['reload'] = Button('reload', {pygame.K_r, pygame.K_4})

        # map
        input_list['map'] = Button('map', {pygame.K_m})

        # horizontal
        input_list['horizontal'] = Axis(
            'horizontal', {(pygame.K_a, pygame.K_d)})

        return input_list
