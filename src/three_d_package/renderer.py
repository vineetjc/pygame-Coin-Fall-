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

        # total time = 18ms

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

        # time = 0ms

        model_matrix = np.matmul(translation_matrix, np.matmul(
            scale_matrix, rot_total_matrix))

        # time = 1ms

        for index, vertex in enumerate(mesh.vertices):
            mesh.mvp_vertices[index] = np.matmul(
                model_matrix, mesh.vertices[index])

        # time = 10ms

        for index, face in enumerate(mesh.faces):
            v0 = mesh.mvp_vertices[face[0]]
            v1 = mesh.mvp_vertices[face[1]]
            v2 = mesh.mvp_vertices[face[2]]

            vd1 = v1 - v0
            vd2 = v2 - v0

            mesh.face_normals[index] = self.cross(vd2[:3], vd1[:3])

            mesh.face_centers[index] = ((v0 + v1 + v2) / 3)[2]

        # time = 0ms

        z_order = np.argsort(mesh.face_centers)

        self.screen.lock()

        # time = 4ms

        mesh.face_light = self.light(mesh.face_normals[:, 0], mesh.face_normals[:, 1], mesh.face_normals[:, 2],
                                     self.light_dir[0], self.light_dir[1], self.light_dir[2],
                                     self.light_intensity, self.ambient_intensity)

        mesh.face_color_r = self.final_color(mesh.face_light, model.color[0])
        mesh.face_color_g = self.final_color(mesh.face_light, model.color[1])
        mesh.face_color_b = self.final_color(mesh.face_light, model.color[2])

        #time1 = time.time()

        for index in z_order:
            if mesh.face_normals[index][2] > 0:
                # time = 0ms

                face_color = (
                    mesh.face_color_r[index], mesh.face_color_g[index], mesh.face_color_b[index])

                # time = 4ms

                face = mesh.faces[index]
                pygame.draw.polygon(self.screen, face_color, [
                    mesh.mvp_vertices[face[0]][:2], mesh.mvp_vertices[face[1]][:2], mesh.mvp_vertices[face[2]][:2]])

        self.screen.unlock()

        #time2 = time.time()

        #print((time2 - time1) * 1000)

    def light(self, face_normals_x, face_normal_y, face_normal_z, light_dir_x, light_dir_y, light_dir_z, light_intensity, ambient_intensity):
        light = face_normals_x * light_dir_x + face_normal_y * \
            light_dir_y + face_normal_z * light_dir_z
        light = light * light_intensity + ambient_intensity
        light = np.clip(light, 0, 1)
        return light

    def final_color(self, face_light, color):
        result = np.multiply(face_light, color)
        return np.uint8(result)

    def cross(self, right, left):
        value = np.array([0.0, 0.0, 0.0])

        value[0] = (left[1] * right[2]) - (left[2] * right[1])
        value[1] = (left[2] * right[0]) - (left[0] * right[2])
        value[2] = (left[0] * right[1]) - (left[1] * right[0])

        length = math.sqrt(value[0] * value[0] + value[1]
                           * value[1] + value[2] * value[2])

        if length != 0:
            value = value / length

        return value
