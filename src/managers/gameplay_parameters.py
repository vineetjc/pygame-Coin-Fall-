##################################################
# Gameplay defining parameters
# Paramerters depend on game mode and difficulty
##################################################


class Gameplay_Parameters:

    def __init__(self):
        self.params_list = {}

        # Classic mode parameters
        #
        # spawn_chance: chance of spawing anything every frame
        # silver_chance: if we have to spawn, chances of silver coin spawning
        # gold_chance: see above
        # bomb_chance: see above
        # Note: all chances in fraction. 0.10 = 10% chance of spawning

        self.params_list['classic_easy'] = {
            'spawn_chance':     0.030,
            'silver_chance':    0.60,
            'gold_chance':      0.30,
            'bomb_chance':      0.10
        }

        self.params_list['classic_medium'] = {
            'spawn_chance':     0.075,
            'silver_chance':    0.55,
            'gold_chance':      0.25,
            'bomb_chance':      0.20
        }

        self.params_list['classic_hard'] = {
            'spawn_chance':     0.120,
            'silver_chance':    0.45,
            'gold_chance':      0.15,
            'bomb_chance':      0.30
        }
