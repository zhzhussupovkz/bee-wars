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
        points = numpy.zeros([48, 2], numpy.uint16)
        for i in range(0, 8):
            for j in range(0, 6):
                points[i * 6 + j][0] = numpy.uint16(random.randint(i * 100, (i + 1) * 100))
                points[i * 6 + j][1] = numpy.uint16(random.randint(j * 100, (j + 1) * 100))
        self.coord = tuple(random.choice(points))
        return Voronoi(points)

    def draw_map(self):
        for i in self.voronoi.ridge_vertices:
            if -1 not in i:
                start_pos = self.voronoi.vertices[i[0]]
                end_pos = self.voronoi.vertices[i[1]]
                pygame.draw.line(self.screen, self.color, start_pos, end_pos)