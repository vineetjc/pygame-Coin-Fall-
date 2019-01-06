import sys
sys.path.append("..")
from input_package.input_manager import *
from load_obj import OBJ_Loader
from classes import Model
from renderer import Renderer
import os
import pygame


def main():
    global width, height, input, renderer, time
    width = 1024
    height = 768
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Coin Fall')
    background = (40, 40, 40)
    time = pygame.time.Clock()

    path = r"E:\Game\KWOC\CoinFall\pygame-Coin-Fall-\res\three_d\reference.objx"
    mesh = OBJ_Loader.load(path)
    model = Model()
    model.mesh = mesh
    model.position = [width // 2, height // 2, 0]
    model.scale = [250, 250, 250]
    model.set_color((255, 215, 0))

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
        r2 = input.get_axis('rotation2')
        r3 = input.get_axis('rotation3') 
        r4 = input.get_axis('rotation4')        

        model.position[0] += h
        model.position[1] += v
        model.scale[0] += r
        model.scale[1] += r
        model.scale[2] += r
        model.rotation[0] += r2 * 0.03
        model.rotation[1] += r3 * 0.03
        model.rotation[2] += r4 * 0.03

        screen.fill(background)
        renderer.render(model)
        print(time.get_fps())
        time.tick()
        pygame.display.flip()


main()
