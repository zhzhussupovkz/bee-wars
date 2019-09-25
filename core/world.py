import pygame
import math
import sys
import random
from core.bee import *

class World():
    SIZE = (640, 640)

    def __init__(self):
        pygame.init()
        self.icon_img = pygame.image.load("./images/world/icon.png")
        pygame.display.set_caption('Bee wars')
        pygame.display.set_icon(self.icon_img)
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.screen.fill((100, 100, 100))
        self.points = []
        self.generate_level()
        self.bee = Bee(self.screen, 320, 320)

    def generate_level(self):
        for i in range(16):
            posx = random.randint(40, 600)
            posy = random.randint(40, 600)
            x, y, z = random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)
            self.points.append([[posx, posy], (x, y, z)])
        
        for x, y in [(x, y) for x in range(self.SIZE[0]) for y in range(self.SIZE[1])]:
            if self.screen.get_at((x, y))[:-1] != (255, 255, 255):
                self.screen.set_at((x, y), min([(math.sqrt((x - i[0][0])**2 + (y - i[0][1])**2), i[1]) for i in self.points])[1])

    def draw(self):
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