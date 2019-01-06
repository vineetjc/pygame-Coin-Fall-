import numpy as np


class Mesh():

    def __init__(self):
        self.vertices = np.zeros((0, 4))
        self.mvp_vertices = np.zeros((0, 4))
        self.mvp_vert_x = np.zeros((0, 4))
        self.mvp_vert_y = np.zeros((0, 4))
        self.mvp_vert_z = np.zeros((0, 4))
        self.faces = np.zeros((0, 3), dtype=int)
        self.face_normals = np.zeros((0, 3))
        self.face_normals_x = np.zeros((0, 3))
        self.face_normals_y = np.zeros((0, 3))
        self.face_normals_z = np.zeros((0, 3))
        self.face_centers = np.zeros(0)
        self.face_color_r = np.zeros(0, np.uint8)
        self.face_color_g = np.zeros(0, np.uint8)
        self.face_color_b = np.zeros(0, np.uint8)
        self.face_light = np.zeros(0)


class Model():

    def __init__(self):
        self.position = [0.0, 0.0, 0.0]
        self.rotation = [0.0, 0.0, 0.0]
        self.scale = [1.0, 1.0, 1.0]
        self.color = np.array([255, 255, 255])
        self.mesh = None

    def set_color(self, color):
        self.color = np.array([color[0], color[1], color[2]])


class Vertex():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Face():

    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3


class Face_Normal():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
