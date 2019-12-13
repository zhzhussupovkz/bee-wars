import pygame
import math
import sys
import random
import datetime
from core.bee import *
from core.map import *
from core.enemy import *
from core.honey import *

class World():
    SIZE = (800, 600)

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.icon_img = pygame.image.load("./images/world/icon.png")
        self.bg = pygame.image.load("./images/world/background.png")
        self.ui = pygame.font.SysFont("monaco", 16)
        pygame.display.set_caption('Bee wars')
        pygame.display.set_icon(self.icon_img)
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.points = []
        self.map = Map(self.screen)
        self.enemies = self._generate_enemies(self.map.enemy_coords)
        self.honey = Honey(self.screen, self.map.honey_coord[0] - 32, self.map.honey_coord[1] - 32)
        self.bee = Bee(self.screen, self.map.coord[0] - 16, self.map.coord[1] - 32)

    def _generate_enemies(self, coords):
        enemies = []
        face = ['left', 'right', 'down', 'up']
        for coord in coords:
            enemies.append(Enemy(self.screen, coord[0] - 16, coord[1] - 32, random.choice(face)))
        return enemies

    def draw(self):
        self.screen.blit(self.bg, [0, 0])
        cyear = datetime.datetime.now().year
        cp = self.ui.render("Copyright (c) %s by zhzhussupovkz" % cyear, 3, (255, 255, 255))
        self.screen.blit(cp, [320, 576])
        self.map.draw_map()
        self.honey.draw()
        self.bee.draw(self.screen)
        self.bee.drawing()
        for enemy in self.enemies:
            enemy.draw(self.screen)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
            self.draw()
            self.bee.update()
            for enemy in self.enemies:
                enemy.update()
            pygame.display.flip()
            self.clock.tick(300)
        pygame.quit()