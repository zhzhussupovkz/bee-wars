import pygame

# player's weapon
class Weapon():
    def __init__(self, screen, player):
        self.player = player
        self.image = pygame.image.load("./images/world/honey-weapon.png")
        self.x, self.y = self.player.x - 4, self.player.y + 8
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.centerx, self.centery = self.rect.center
        self.screen = screen
        self.drawing, self.last_direction = False, self.player.face

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.centerx, self.centery = self.rect.center
        if self.drawing:
            if self.last_direction == 'left':
                if self.x >= 2:
                    self.x -= 4
            elif self.last_direction == 'right':
                if self.x <= 796:
                    self.x += 4
            elif self.last_direction == 'up':
                if self.y >= 2:
                    self.y -= 4
            elif self.last_direction == 'down':
                if self.y <= 796:
                    self.y += 4
            if self.x <= 4 or self.x >= 796 or self.y <= 4 or self.y >= 596:
                self.drawing = False
                self.last_direction = self.player.face
        else:
            self.last_direction = self.player.face
            if self.player.face == 'left':
                self.x, self.y = self.player.x + 12, self.player.y + 20
            elif self.player.face == 'right':
                self.x, self.y = self.player.x + 12, self.player.y + 20
            elif self.player.face == 'up':
                self.x, self.y = self.player.x + 20, self.player.y + 16
            elif self.player.face == 'down':
                self.x, self.y = self.player.x + 20, self.player.y + 16