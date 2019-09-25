import numpy
import random
import pygame
from scipy.spatial import Voronoi

class Map():
    def __init__(self, screen):
        self.screen = screen

    def __generate_voronoi(self):
        points = numpy.zeros([640, 2], numpy.uint16)
        for i in range(0, 640, 16):
            points[i][0] = numpy.uint16(random.randint(0, 640))
            points[i][1] = numpy.uint16(random.randint(0, 640))
        return Voronoi(points)

    def draw_map(self):
        voronoi = self.__generate_voronoi()
        for i in voronoi.ridge_vertices:
            if -1 not in i:
                start_pos = voronoi.vertices[i[0]]
                end_pos = voronoi.vertices[i[1]]
                pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos)