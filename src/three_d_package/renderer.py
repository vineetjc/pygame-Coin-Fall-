import numpy as np
import pygame
import math
import time


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

        mesh.mvp_vert_x = mesh.mvp_vertices[:, 0]
        mesh.mvp_vert_y = mesh.mvp_vertices[:, 1]
        mesh.mvp_vert_z = mesh.mvp_vertices[:, 2]

        for index, face in enumerate(mesh.faces):
            a1 = mesh.mvp_vert_x[face[1]] - mesh.mvp_vert_x[face[0]]
            a2 = mesh.mvp_vert_y[face[1]] - mesh.mvp_vert_y[face[0]]
            a3 = mesh.mvp_vert_z[face[1]] - mesh.mvp_vert_z[face[0]]

            b1 = mesh.mvp_vert_x[face[2]] - mesh.mvp_vert_x[face[0]]
            b2 = mesh.mvp_vert_y[face[2]] - mesh.mvp_vert_y[face[0]]
            b3 = mesh.mvp_vert_z[face[2]] - mesh.mvp_vert_z[face[0]]

            mesh.face_normals_x[index] = (a2 * b3) - (a3 * b2)
            mesh.face_normals_y[index] = (a1 * b3) - (a3 * b1)
            mesh.face_normals_z[index] = (a1 * b2) - (a2 * b1)

            length = math.sqrt(mesh.face_normals_x[index] * mesh.face_normals_x[index] +
                               mesh.face_normals_y[index] * mesh.face_normals_y[index] +
                               mesh.face_normals_z[index] * mesh.face_normals_z[index])

            if length != 0:
                mesh.face_normals_x[index] = mesh.face_normals_x[index] / length
                mesh.face_normals_y[index] = mesh.face_normals_y[index] / length
                mesh.face_normals_z[index] = mesh.face_normals_z[index] / length

            mesh.face_centers[index] = (
                mesh.mvp_vert_z[face[0]] + mesh.mvp_vert_z[face[0]] + mesh.mvp_vert_z[face[0]]) / 3

        z_order = np.argsort(mesh.face_centers)

        mesh.face_light = self.light(mesh.face_normals_x,  mesh.face_normals_y,  mesh.face_normals_z,
                                     self.light_dir[0], self.light_dir[1], self.light_dir[2],
                                     self.light_intensity, self.ambient_intensity)

        mesh.face_color_r = self.final_color(mesh.face_light, model.color[0])
        mesh.face_color_g = self.final_color(mesh.face_light, model.color[1])
        mesh.face_color_b = self.final_color(mesh.face_light, model.color[2])

        self.screen.lock()

        for index in np.nditer(z_order):
            if mesh.face_normals_z[index] >= 0:
                face_color = (
                    mesh.face_color_r[index], mesh.face_color_g[index], mesh.face_color_b[index])

                face = mesh.faces[index]
                v0 = face[0]
                v1 = face[1]
                v2 = face[2]

                pygame.draw.polygon(self.screen, face_color, [
                    [mesh.mvp_vert_x[v0], mesh.mvp_vert_y[v0]],
                    [mesh.mvp_vert_x[v1], mesh.mvp_vert_y[v1]],
                    [mesh.mvp_vert_x[v2], mesh.mvp_vert_y[v2]]
                ])

        self.screen.unlock()

    def light(self, face_normals_x, face_normal_y, face_normal_z, light_dir_x, light_dir_y, light_dir_z, light_intensity, ambient_intensity):
        light = face_normals_x * light_dir_x + face_normal_y * \
            light_dir_y + face_normal_z * light_dir_z
        light = light * light_intensity + ambient_intensity
        light = np.clip(light, 0, 1)
        return light

    def final_color(self, face_light, color):
        result = np.multiply(face_light, color)
        return np.uint8(result)
