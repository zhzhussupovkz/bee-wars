import pygame

# Bee sprite
class BeeSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(BeeSprite, self).__init__()
        self.screen = screen
        self.left, self.right, self.up, self.down = [], [], [], []
        for i in range(3):
            self.left.append(pygame.image.load("./images/bee/bee-left_{}.png".format(i+1)))
            self.right.append(pygame.image.load("./images/bee/bee-right_{}.png".format(i+1)))
            self.down.append(pygame.image.load("./images/bee/bee-down_{}.png".format(i+1)))
            self.up.append(pygame.image.load("./images/bee/bee-up_{}.png".format(i+1)))

        self.index = 0
        self.image = self.right[self.index]
        self.x, self.y, self.face = x, y, 'right'
        self.rect = pygame.Rect(self.x, self.y, 64, 64)

    def move_left(self):
        self.face = 'left'
        self.index += 1
        if self.index >= len(self.left) * 10:
            self.index = 0
        if self.index % 10 == 0:
            self.image = self.left[int(self.index/10)]
        self.rect = pygame.Rect(self.x - 0.75, self.y, 64, 64)
        self.x -= 0.75

    def move_right(self):
        self.face = 'right'
        self.index += 1
        if self.index >= len(self.right) * 10:
            self.index = 0
        if self.index % 10 == 0:
            self.image = self.right[int(self.index/10)]
        self.rect = pygame.Rect(self.x + 0.75, self.y, 64, 64)
        self.x += 0.75

    def move_down(self):
        self.face = 'down'
        self.index += 1
        if self.index >= len(self.down) * 10:
            self.index = 0
        if self.index % 10 == 0:
            self.image = self.down[int(self.index/10)]
        self.rect = pygame.Rect(self.x, self.y + 0.75, 64, 64)
        self.y += 0.75

    def move_up(self):
        self.face = 'up'
        self.index += 1
        if self.index >= len(self.up) * 10:
            self.index = 0
        if self.index % 10 == 0:
            self.image = self.up[int(self.index/10)]
        self.rect = pygame.Rect(self.x, self.y - 0.75, 64, 64)
        self.y -= 0.75

    def update(self):
        super(BeeSprite, self).update()

# Bee class - main player
class Bee(pygame.sprite.Group):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.bee_sprite = BeeSprite(self.screen, x, y)
        self.x, self.y = self.bee_sprite.x, self.bee_sprite.y
        self.face, self.centerx, self.centery = 'right', self.bee_sprite.rect.centerx, self.bee_sprite.rect.centery
        super(Bee, self).__init__(self.bee_sprite)

    def update(self):
        self.face = self.bee_sprite.face
        self.x, self.y = self.bee_sprite.x, self.bee_sprite.y
        self.centerx, self.centery = self.bee_sprite.rect.centerx, self.bee_sprite.rect.centery
        self.walk()
        super(Bee, self).update()

    def move_left(self):
        self.bee_sprite.move_left()

    def move_right(self):
        self.bee_sprite.move_right()

    def move_down(self):
        self.bee_sprite.move_down()

    def move_up(self):
        self.bee_sprite.move_up()

    def walk(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and self.x <= 732:
            self.move_right()
        elif key[pygame.K_LEFT] and self.x >= 16:
            self.move_left()
        if key[pygame.K_UP] and self.y >= 16:
            self.move_up()
        elif key[pygame.K_DOWN] and self.y <= 532:
            self.move_down()
