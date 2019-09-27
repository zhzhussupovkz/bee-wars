import pygame
import math
import sys
import random
from core.bee import *
from core.map import *

class World():
    SIZE = (800, 600)

    def __init__(self):
        pygame.init()
        self.icon_img = pygame.image.load("./images/world/icon.png")
        self.bg = pygame.image.load("./images/world/background.png")
        pygame.display.set_caption('Bee wars')
        pygame.display.set_icon(self.icon_img)
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.points = []
        self.map = Map(self.screen)
        self.bee = Bee(self.screen, self.map.coord[0] - 32, self.map.coord[1] - 32)

    def draw(self):
        self.screen.blit(self.bg, [0, 0])
        self.map.draw_map()
        self.bee.draw()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
            self.draw()
            self.bee.walk()
            pygame.display.flip()
        pygame.quit()