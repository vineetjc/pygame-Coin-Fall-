###############################
# Saves and loads highscore
###############################

import json
import os.path


class Highscore_Manager():

    def __init__(self):
        self.load_highscore_from_file()

    def load_highscore_from_file(self):
        if os.path.isfile('highscore.data'):
            highscore_file = open('highscore.data', 'r')
            self.data = json.load(highscore_file)
            highscore_file.close()
        else:
            self.data = dict()
            self.data['classic_easy'] = 0
            self.data['classic_medium'] = 0
            self.data['classic_hard'] = 0
            self.data['infinite'] = 0
            self.data['1v1'] = 0
            self.data['ai'] = 0
            self.data['hardcore'] = 0
            self.data['heist'] = 0

            self.save_highscore_to_file()

    def save_highscore_to_file(self):
        highscore_file = open('highscore.data', 'w')
        json.dump(self.data, highscore_file, indent=4)
        highscore_file.close()

    def reset_highscore(self):
        self.data = dict()
        self.data['classic_easy'] = 0
        self.data['classic_medium'] = 0
        self.data['classic_hard'] = 0
        self.data['infinite'] = 0
        self.data['1v1'] = 0
        self.data['ai'] = 0
        self.data['hardcore'] = 0
        self.data['heist'] = 0

        self.save_highscore_to_file()
