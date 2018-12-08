##########################################
# manages settings
# will write and read from settings file
# will be updated from the settings menu
###########################################

import json
import os.path

# template for the data that will be serialised and saved as json
settings_data = dict(
    player_name="",
    sound_level=5,
    mute=False
)


class Settings_Manager():

    def __init__(self):
        self.load_settings_from_file()

    def load_settings_from_file(self):
        if os.path.isfile('../settings.config'):
            settings_file = open('../settings.config', 'r')
            self.settings_data = json.load(settings_file)
            settings_file.close()
        else:
            self.settings_data = dict(
                player_name="player",
                sound_level=5,
                mute=False
            )
            self.save_settings_to_file()

    def save_settings_to_file(self):
        settings_file = open('../settings.config', 'w')
        json.dump(self.settings_data, settings_file, indent=4)
        settings_file.close()

