import pygame

class Bee():
    def __init__(self, screen, x, y):
        self.image = pygame.image.load('./images/bee/bee.png')
        self.x, self.y = x, y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])
    
    def move_left(self):
        self.x -= 0.8
        if self.x <= 16:
            self.x = 16

    def move_right(self):
        self.x += 0.8
        if self.x >= 560:
            self.x = 560

    def move_down(self):
        if self.y <= 560:
            self.y += 0.8
    
    def move_up(self):
        if self.y >= 16:
            self.y -= 0.8

    def walk(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.move_right()
        elif key[pygame.K_LEFT]:
            self.move_left()
        if key[pygame.K_UP]:
            self.move_up()
        elif key[pygame.K_DOWN]:
            self.move_down()