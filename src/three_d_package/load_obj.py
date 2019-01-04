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
            elif values[0] == 'f':
                new_face = [int(values[1]) - 1, int(values[2]
                                                    ) - 1, int(values[3]) - 1]
                mesh.faces = np.vstack((mesh.faces, new_face))

        for face in mesh.faces:
            v1 = mesh.vertices[face[1]] - mesh.vertices[face[0]]
            v2 = mesh.vertices[face[2]] - mesh.vertices[face[0]]
            face_normal = np.cross(v1[:3], v2[:3])
            length = np.sqrt((np.sum(face_normal**2)))
            if length is not 0:
                face_normal = face_normal / length

            mesh.face_normals = np.vstack((mesh.face_normals, face_normal))

        return mesh
