import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("ressources/background.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)