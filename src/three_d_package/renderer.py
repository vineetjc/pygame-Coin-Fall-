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

        rx = model.scale[0]
        ry = model.scale[1]
        rz = model.scale[2]

        cx = math.cos(model.rotation[0])
        sx = math.sin(model.rotation[0])
        cy = math.cos(model.rotation[1])
        sy = math.sin(model.rotation[1])
        cz = math.cos(model.rotation[2])
        sz = math.sin(model.rotation[2])

        scale_matrix = np.array([[rx, 00, 00, 00],
                                 [00, ry, 00, 00],
                                 [00, 00, rz, 00],
                                 [00, 00, 00, 1]])

        translation_matrix = np.array([[1, 00, 00, dx],
                                       [00, 1, 00, dy],
                                       [00, 00, 1, dz],
                                       [00, 00, 00, 1]])

        rot_total_matrix = np.array([
            [cy * cz,                   cy * sz,                    -sy,        0],
            [sx * sy * cz - cx * sz,    sx * sy * sz + cx * cz,     sx * cy,    0],
            [cx * sy * cz + sx * sz,    cx * sy * sz - sx * cz,     cx * cy,    0],
            [0,                         0,                          0,          1]
        ])

        model_matrix = np.matmul(translation_matrix, np.matmul(
            scale_matrix, rot_total_matrix))

        for index, vertex in enumerate(mesh.vertices):
            mesh.mvp_vertices[index] = np.matmul(
                model_matrix, mesh.vertices[index])

        for index, face in enumerate(mesh.faces):
            v1 = mesh.mvp_vertices[face[1]] - mesh.mvp_vertices[face[0]]
            v2 = mesh.mvp_vertices[face[2]] - mesh.mvp_vertices[face[0]]
            face_normal = np.cross(v1[:3], v2[:3])
            length = np.sqrt((np.sum(face_normal**2)))

            if length is not 0:
                face_normal = face_normal / length

            mesh.face_normals[index] = face_normal

        for index, face in enumerate(mesh.faces):
            if mesh.face_normals[index][2] > 0:
                color = self.get_color(model.color, mesh.face_normals[index])
                if color is not [0, 0, 0]:
                    pygame.draw.polygon(self.screen, color, [
                                        mesh.mvp_vertices[face[0]][:2], mesh.mvp_vertices[face[1]][:2], mesh.mvp_vertices[face[2]][:2]])

    def get_color(self, color, face_normal):
        face_light = np.dot(face_normal, self.light_dir) * \
            self.light_intensity + self.ambient_intensity

        if face_light < 0:
            return [0, 0, 0]

        face_light = min(face_light, 1.0)
        return face_light * color
