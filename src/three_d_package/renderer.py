import numpy as np
import pygame
import math


class Renderer():

    def __init__(self, screen, camera_pos, screen_width, screen_height, light_dir, light_intensity, ambient_intensity):
        self.screen = screen
        self.camera_pos = camera_pos
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.light_dir = np.array(light_dir)
        length = np.sqrt((np.sum(self.light_dir**2)))
        if length is not 0:
            self.light_dir = self.light_dir / length

        self.light_intensity = light_intensity
        self.ambient_intensity = ambient_intensity

    def render(self, model):
        mesh = model.mesh

        dx = model.position[0]
        dy = model.position[1]
        dz = model.position[2]

        sx = model.scale[0]
        sy = model.scale[1]
        sz = model.scale[2]

        MVP = np.array([[sx, 00, 00, dx],
                        [00, sy, 00, dy],
                        [00, 00, sz, dz],
                        [00, 00, 00,  1]])

        for index, vertex in enumerate(mesh.vertices):
            mesh.mvp_vertices[index] = self.multi_MVP(
                mesh.vertices[index], MVP)

        for index, face in enumerate(mesh.faces):
            if mesh.face_normals[index][2] > 0:
                color = self.get_color(model.color, mesh.face_normals[index])
                if color is not [0, 0, 0]:
                    pygame.draw.polygon(self.screen, color, [
                                        mesh.mvp_vertices[face[0]][:2], mesh.mvp_vertices[face[1]][:2], mesh.mvp_vertices[face[2]][:2]])

    def get_color(self, color, face_normal):
        face_light = np.dot(face_normal, self.light_dir) * self.light_intensity + self.ambient_intensity

        if face_light < 0:
            return [0, 0, 0]

        face_light = min(face_light, 1.0)
        return face_light * color

    def multi_MVP(self, vertex, MVP):
        result = [
            vertex[0] * MVP[0][0] + vertex[1] * MVP[0][1] +
            vertex[2] * MVP[0][2] + vertex[3] * MVP[0][3],

            vertex[0] * MVP[1][0] + vertex[1] * MVP[1][1] +
            vertex[2] * MVP[1][2] + vertex[3] * MVP[1][3],

            vertex[0] * MVP[2][0] + vertex[1] * MVP[2][1] +
            vertex[2] * MVP[2][2] + vertex[3] * MVP[2][3],

            vertex[0] * MVP[3][0] + vertex[1] * MVP[3][1] +
            vertex[2] * MVP[3][2] + vertex[3] * MVP[3][3]
        ]

        return result
