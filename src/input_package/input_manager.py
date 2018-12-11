###############################################################
# Manages input
# Will act as a wrapper around the pygame input functionality
# and provide ease of use for common input tasks
# Will support:
#   multiple keys for same action
#   axis input (three possible input: -1, 0, 1)
#   joystick input
###############################################################

from .input_button import Button
from .input_axis import Axis
import pygame.key


class Input_Manager():
    ''' Will have the states of all the buttons and axis defined by the game.
        These states can be retrieved from here with simple functions
        Will get these states at the start of the frame
    '''

    def __init__(self):
        self.input_list = self.get_input_list()

    def update(self, events):
        for key in self.input_list:
            self.input_list[key].reset_values()

        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.handle_keyboard_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_event(event)

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

    def handle_keyboard_event(self, event):
        for key in self.input_list:
            self.input_list[key].set_value(event)

    def handle_mouse_event(self, evnet):
        pass
