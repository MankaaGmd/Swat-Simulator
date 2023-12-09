import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ressources/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()