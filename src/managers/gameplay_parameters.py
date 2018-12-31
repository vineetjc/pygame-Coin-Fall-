##################################################
# Gameplay defining parameters
# Paramerters depend on game mode and difficulty
##################################################
from src.misc.game_enums import Game_Mode


class Gameplay_Parameters:

    def __init__(self):
        self.params_list = {}

        #
        #
        #
        # Classic mode parameters
        #
        # display_name: display name is game introduction screen
        # introduction: intoduction text in the game introduction screen
        # game_mode: Enum for game mode
        # score_multiplier: -
        # spawn_chance: chance of spawing anything every frame
        # silver_chance: if we have to spawn, chances of silver coin spawning
        # gold_chance: see above
        # bomb_chance: see above
        # Note: all chances in fraction. 0.10 = 10% chance of spawning

        self.params_list['classic_easy'] = {
            'key':              'classic_easy',
            'display_name':     'Classic Mode',
            'game_over_name':   'Classic Easy Mode',
            'introduction':     ('The classic game mode, avoid bombs and '
                                 'collect as many coins as possible in 30 seconds.'
                                 ),
            'game_mode':        Game_Mode.CLASSIC,
            'score_multiplier': 1.0,
            'spawn_chance':     0.030,
            'silver_chance':    0.60,
            'gold_chance':      0.30,
            'bomb_chance':      0.10
        }

        self.params_list['classic_medium'] = {
            'key':              'classic_medium',
            'display_name':     'Classic Mode',
            'game_over_name':   'Classic Medium Mode',
            'introduction':     ('The classic game mode, avoid bombs and '
                                 'collect as many coins as possible in 30 seconds.'
                                 ),
            'game_mode':        Game_Mode.CLASSIC,
            'score_multiplier': 3.0,
            'spawn_chance':     0.075,
            'silver_chance':    0.55,
            'gold_chance':      0.25,
            'bomb_chance':      0.20
        }

        self.params_list['classic_hard'] = {
            'key':              'classic_hard',
            'display_name':     'Classic Mode',
            'game_over_name':   'Classic Hard Mode',
            'introduction':     ('The classic game mode, avoid bombs and '
                                 'collect as many coins as possible in 30 seconds.'
                                 ),
            'game_mode':        Game_Mode.CLASSIC,
            'score_multiplier': 5.0,
            'spawn_chance':     0.120,
            'silver_chance':    0.45,
            'gold_chance':      0.15,
            'bomb_chance':      0.30
        }

        #
        #
        #
        # Infinite mode parameters
        #
        # display_name: display name is game introduction screen
        # introduction: intoduction text in the game introduction screen
        # game_mode: Enum for game mode
        # score_multiplier: -
        # spawn_chance: chance of spawing anything every frame
        # silver_chance: if we have to spawn, chances of silver coin spawning
        # gold_chance: see above
        # bomb_chance: see above
        # Note: all chances in fraction. 0.10 = 10% chance of spawning

        self.params_list['infinite'] = {
            'key':              'infinite',
            'display_name':     'Infinite Mode',
            'game_over_name':   'Infinite Mode',
            'introduction':     ('The infinite game mode, avoid bombs and '
                                 'collect as many coins as possible without.'
                                 'the time limit.'
                                 ),
            'game_mode':        Game_Mode.INFINITE,
            'score_multiplier': 3.0,
            'spawn_chance':     0.075,
            'silver_chance':    0.55,
            'gold_chance':      0.25,
            'bomb_chance':      0.20
        }

        #
        #
        #
        # 1 v 1 mode parameters
        #
        # display_name: display name is game introduction screen
        # introduction: intoduction text in the game introduction screen
        # game_mode: Enum for game mode
        # score_multiplier: -
        # spawn_chance: chance of spawing anything every frame
        # silver_chance: if we have to spawn, chances of silver coin spawning
        # gold_chance: see above
        # bomb_chance: see above
        # Note: all chances in fraction. 0.10 = 10% chance of spawning

        self.params_list['1v1'] = {
            'key':              '1v1',
            'display_name':     '1 v 1 Mode',
            'game_over_name':   '1 v 1 Mode',
            'introduction':     ('The 1 v 1 game mode, '
                                 'Player 1 (Blue) controls by WASD, '
                                 'Player 2 (Red) controls by Arrow Keys.'
                                 ),
            'game_mode':        Game_Mode.ONE_V_ONE,
            'score_multiplier': 3.0,
            'spawn_chance':     0.075,
            'silver_chance':    0.55,
            'gold_chance':      0.25,
            'bomb_chance':      0.20
        }

        #
        #
        #
        # AI mode parameters
        #
        # display_name: display name is game introduction screen
        # introduction: intoduction text in the game introduction screen
        # game_mode: Enum for game mode
        # score_multiplier: -
        # spawn_chance: chance of spawing anything every frame
        # silver_chance: if we have to spawn, chances of silver coin spawning
        # gold_chance: see above
        # bomb_chance: see above
        # Note: all chances in fraction. 0.10 = 10% chance of spawning

        self.params_list['ai'] = {
            'key':              'ai',
            'display_name':     'AI Mode',
            'game_over_name':   'AI Mode',
            'introduction':     ('The AI game mode, design you own AI to '
                                 'compete for AI highscore.'
                                 ),
            'game_mode':        Game_Mode.AI,
            'score_multiplier': 3.0,
            'spawn_chance':     0.075,
            'silver_chance':    0.55,
            'gold_chance':      0.25,
            'bomb_chance':      0.20
        }

        #
        #
        #
        # Hardcore mode parameters
        #
        # display_name: display name is game introduction screen
        # introduction: intoduction text in the game introduction screen
        # game_mode: Enum for game mode
        # score_multiplier: -
        # spawn_chance: chance of spawing anything every frame
        # silver_chance: if we have to spawn, chances of silver coin spawning
        # gold_chance: see above
        # bomb_chance: see above
        # Note: all chances in fraction. 0.10 = 10% chance of spawning

        self.params_list['hardcore'] = {
            'key':              'hardcore',
            'display_name':     'Hardcore Mode',
            'game_over_name':   'Hardcore Mode',
            'introduction':     ('The hardcore game mode, try to survive '
                                 'long as you can in a rain on bombs.'
                                 ),
            'game_mode':        Game_Mode.HARDCORE,
            'score_multiplier': 5.0,
            'spawn_chance':     0.075,
            'silver_chance':    0.00,
            'gold_chance':      0.00,
            'bomb_chance':      1.00
        }

        #
        #
        #
        # Heist mode parameters
        #
        # display_name: display name is game introduction screen
        # introduction: intoduction text in the game introduction screen
        # game_mode: Enum for game mode
        # score_multiplier: -
        # spawn_chance: chance of spawing anything every frame
        # silver_chance: if we have to spawn, chances of silver coin spawning
        # gold_chance: see above
        # bomb_chance: see above
        # Note: all chances in fraction. 0.10 = 10% chance of spawning

        self.params_list['heist'] = {
            'key':              'heist',
            'display_name':     'Heist Mode',
            'game_over_name':   'Heist Mode',
            'introduction':     ('The Heist game mode, collect as many '
                                 'coins as you can but don\'t miss 4 '
                                 'coins in a row.'
                                 ),
            'game_mode':        Game_Mode.HEIST,
            'score_multiplier': 3.0,
            'spawn_chance':     0.030,
            'silver_chance':    0.00,
            'gold_chance':      1.00,
            'bomb_chance':      0.00
        }
