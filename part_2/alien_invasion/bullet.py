import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядом, выпущенным кораблем."""

    def __init__(self, ai_game):
        """Создает объект снаряда в текущей позиции корабля."""
        super().__init__() # класс Bullet наследует от класса Sprite в pygame
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # создание снаряда в позиции (0, 0) и перемещение к середине верхней части корабля:
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # позиция снаряда хранится в вещественном формате:
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        # обновление точной позиции снаряда:
        self.y -= self.settings.bullet_speed
        # обновление позиции прямоугольникка:
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Выводит снаряд на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)