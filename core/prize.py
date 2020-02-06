
import pygame

# player's prize
class Prize():
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("./images/world/prize.png")
        self.screen, self.x, self.y = screen, x, y
        self.drawing = False

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    def update(self):
        if self.drawing and self.y <= 720:
            self.y += 2
