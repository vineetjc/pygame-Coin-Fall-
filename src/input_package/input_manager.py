###############################################################
# Manages input
# Will act as a wrapper around the pygame input functionality
# and provide ease of use for common input tasks
# Will support:
#   multiple keys for same action
#   axis input (three possible input: -1, 0, 1)
#   joystick input
#
# Define your input scheme at input_scheme.py
###############################################################

from .input_button import Button
from .input_axis import Axis
from .input_scheme import *
import pygame.key


class Input_Manager():
    ''' 
    Will have the states of all the buttons and axis defined by the game.
    These states can be retrieved from here with simple functions
    Will get these states at the start of the frame
    '''

    def __init__(self):
        self.input_list = get_input_list()

    def update(self, events):
        # for key in self.input_list:
        #   self.input_list[key].reset_values()

        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.handle_keyboard_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_event(event)

    def get_button(self, button_name):
        ''' 
        Gets the state of a user defined button
        :param button_name: the button name as defined in input_manager
        :return True if button is pressed down state, False otherwise
        '''

        return self.input_list[button_name].get_value()

    def get_axis(self, axis_name):
        pass

    def handle_keyboard_event(self, event):
        for key in self.input_list:
            self.input_list[key].set_value(event)

    def handle_mouse_event(self, evnet):
        pass
