###################################
# Base class for input types like
# Buttons and Axis
###################################

class Input():

    def __init__(self):
        pass

    def reset_values(self):
        self.value = 0

    def set_value(self, event):
        pass

    def get_value(self):
        pass