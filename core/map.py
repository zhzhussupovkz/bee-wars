import numpy
import random
import pygame
from scipy.spatial import Voronoi

class Map():
    def __init__(self, screen):
        self.screen = screen
        self.voronoi = self.__generate_voronoi()
        self.color = (0, 0, 128)

    def __generate_voronoi(self):
        points = numpy.zeros([832, 2], numpy.uint16)
        for i in range(-32, 832, 32):
            points[i][0] = numpy.uint16(random.randint(0, 800))
            points[i][1] = numpy.uint16(random.randint(0, 400))
        return Voronoi(points)

    def draw_map(self):
        for i in self.voronoi.ridge_vertices:
            if -1 not in i:
                start_pos = self.voronoi.vertices[i[0]]
                end_pos = self.voronoi.vertices[i[1]]
                pygame.draw.line(self.screen, self.color, start_pos, end_pos)