import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий пришельца."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # загрузка изображения пришельца и назначание атрибута rect:
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу экрана,
        # удаленном от левого края на ширину пришельца, и удаленном от
        # верха экрана на высоту пришельца:
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца:
        self.x = float(self.rect.x)


    def update(self):
        """Перемещает пришельца."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    
    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        return (self.rect.right >= self.screen_rect.right) or (self.rect.left <= 0)
    
