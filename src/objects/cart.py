##################
# Cart Class
##################
from src.misc.game_enums import Entity


class Cart(object):
    def __init__(self, res, size, surface):
        self.type = Entity.CART
        self.surface = surface
        self.image = res.cart_img
        self.x = (size[0] / 2) - 80
        self.y = size[1] - 120
        self.points = 0  # Changed Points to points
        self.dead = False  # Add this for game end check

    def handle_keys(self, pygame, size):
        key = pygame.key.get_pressed()
        dist = 10  # Change this value if necessary
        if key[pygame.K_RIGHT]:
            if self.x < size[0] - 140:
                self.x += dist

        elif key[pygame.K_LEFT]:
            if self.x > -10:
                self.x -= dist

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

    def collect_item(self, pygame, res, coin):
        if 645 > coin.y > 633:
            if ((self.x < coin.x + (55.0 / 2) < self.x + 160) and
                    (self.x < coin.x) and (self.x + 160 > coin.x + 55)):
                try:
                    if not coin.collected:
                        if coin.type == Entity.BLUE_COIN:
                            self.points += 3  # Bonus coin
                        elif coin.type == Entity.BOMB:
                            pygame.time.delay(500)
                            self.dead = True  # Replace quit with death
                        else:
                            self.points += 1

                        coin.collect()
                except AttributeError:
                    pass
