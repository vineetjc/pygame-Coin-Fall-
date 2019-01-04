import sys
sys.path.append("..")
from input_package.input_manager import *
from load_obj import OBJ_Loader
from classes import Model
from renderer import Renderer
import os
import pygame


def main():
    global width, height, input, renderer
    width = 1024
    height = 768
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Coin Fall')
    background = (40, 40, 40)

    path = r"E:\Game\KWOC\CoinFall\pygame-Coin-Fall-\res\three_d\bomb.objx"
    mesh = OBJ_Loader.load(path)
    model = Model()
    model.mesh = mesh
    model.position = [width // 2, height // 2, 0]
    model.scale = [200, 200, 200]
    model.set_color((250, 250, 150))

    input = Input_Manager()
    renderer = Renderer(screen, [512, 384, 0], 1024, 768, [1, -1, 1], 0.8, 0.1)
    game_loop(screen, background, model)


def game_loop(screen, background, model):
    running = True
    while running:
        events = pygame.event.get()
        input.update(events)

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        h = input.get_axis('horizontal')
        v = input.get_axis('vertical')
        r = input.get_axis('rotation')

        model.position[0] += h
        model.position[1] += v
        model.scale[0] += r
        model.scale[1] += r
        model.scale[2] += r

        screen.fill(background)
        renderer.render(model)
        pygame.display.flip()


main()
