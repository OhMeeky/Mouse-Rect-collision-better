import pygame

class Grid(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
