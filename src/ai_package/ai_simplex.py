####################################
# Example AI using simplex noise
# It simply moves the AI randomly
####################################
from .ai_base import AI_Base
from src.simplex_noise_package.noise import PerlinNoise, normalize


class AI_Simplex(AI_Base):

    def __init__(self):
        self.pn = PerlinNoise(num_octaves=7, persistence=0.1)
        self.noise_index = 0

    def restart(self):
        self.noise_index = 0

    def update(self, entity_list, cart):
        self.noise_index += 1
        random_movement = normalize(self.pn.noise(self.noise_index)) * 2 - 1

        if abs(random_movement) < 0.02:
            random_movement = 0
        
        return random_movement
