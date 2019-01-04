from load_obj import OBJ_Loader
from classes import Model
import os
import pygame


def main():
    global width, height 
    width = 1024
    height = 768
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Coin Fall')
    background = (40, 40, 40)

    path = r"E:\Game\KWOC\CoinFall\pygame-Coin-Fall-\res\three_d\sphere.objx"
    mesh = OBJ_Loader.load(path)
    model = Model()
    model.mesh = mesh
    model.position = [width // 2, height // 2, 0]
    model.scale = [200, 200, 200]

    game_loop(screen, background, model)


def game_loop(screen, background, model):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(background)

        mesh = model.mesh

        for face, face_normal in zip(mesh.faces, mesh.face_normals):
            if face_normal[2] > 0:
                pygame.draw.polygon(screen, normal_to_color(face_normal),
                                    transform(mesh, face))

        for face, face_normal in zip(mesh.faces, mesh.face_normals):
            if face_normal[2] > 0:
                pygame.draw.polygon(screen, (50, 50, 50),
                                    transform(mesh, face), 1)

        pygame.display.flip()


def transform_vertex(vertex):
    scale = 300
    vertex_new = [
        width // 2 + int(vertex[0] * scale),
        height // 2 + int(vertex[1] * scale)
    ]
    return vertex_new


def normal_to_color(face_normal):
    return ((face_normal[0] / 2 + 0.5) * 255, (face_normal[1] / 2 + 0.5) * 255, (face_normal[2] / 2 + 0.5) * 255)


def transform(mesh, face):
    scale = 300

    vertex_list = [[
        width // 2 + int(mesh.vertices[face[0]][0] * scale),
        height // 2 + int(mesh.vertices[face[0]][1] * scale)
    ],

        [
        width // 2 + int(mesh.vertices[face[1]][0] * scale),
        height // 2 + int(mesh.vertices[face[1]][1] * scale)
    ],

        [
        width // 2 + int(mesh.vertices[face[2]][0] * scale),
        height // 2 + int(mesh.vertices[face[2]][1] * scale)
    ]]

    return vertex_list


main()
