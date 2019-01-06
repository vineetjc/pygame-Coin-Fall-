from classes import *
import numpy as np


class OBJ_Loader():

    def __init__(self):
        pass

    @staticmethod
    def load(file_name):
        mesh = Mesh()

        for line in open(file_name, 'r'):
            if line.startswith('#'):
                continue

            values = line.split()

            if not values:
                continue

            if values[0] == 'v':
                new_vertex = [float(values[1]), float(
                    values[2]), float(values[3]), 1.0]
                mesh.vertices = np.vstack((mesh.vertices, new_vertex))
                mesh.mvp_vertices = np.vstack((mesh.mvp_vertices, new_vertex))
            elif values[0] == 'f':
                new_face = [int(values[1]) - 1, int(values[2]
                                                    ) - 1, int(values[3]) - 1]
                mesh.faces = np.vstack((mesh.faces, new_face))

        for index, face in enumerate(mesh.faces):
            v0 = mesh.vertices[face[0]]
            v1 = mesh.vertices[face[1]]
            v2 = mesh.vertices[face[2]]

            vd1 = v1 - v0
            vd2 = v2 - v0

            face_normal = np.cross(vd1[:3], vd2[:3])
            length = np.sqrt((np.sum(face_normal**2)))

            if length is not 0:
                face_normal = face_normal / length

            mesh.face_normals = np.vstack((mesh.face_normals, face_normal))

            mesh.face_normals_x = mesh.face_normals[:, 0]
            mesh.face_normals_y = mesh.face_normals[:, 1]
            mesh.face_normals_z = mesh.face_normals[:, 2]

            mesh.face_centers = np.append(
                mesh.face_centers, ((v0 + v1 + v2) / 3)[2])

            mesh.face_color_r = np.append(mesh.face_color_r, np.uint8(255))
            mesh.face_color_g = np.append(mesh.face_color_g, np.uint8(255))
            mesh.face_color_b = np.append(mesh.face_color_b, np.uint8(255))

            mesh.face_light = np.append(mesh.face_light, 0.0)

        return mesh
