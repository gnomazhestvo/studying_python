import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс управления снарядами."""

    def __init__(self, shooter):
        super().__init__()
        self.screen = shooter.screen
        self.color = (0, 0, 0)
        self.bullet_width = 15
        self.bullet_height = 3
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midleft = shooter.gun.rect.midleft
        self.x = float(self.rect.x)

    def update(self):
        self.x += 5
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)