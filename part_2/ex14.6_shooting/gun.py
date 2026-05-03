import pygame

class Gun:
    """Класс управления пушкой."""
    
    def __init__(self, shooter):
        """Инициализирует пушку и выводит его в начальной позиции."""
        # экран:
        self.screen = shooter.screen
        self.screen_rect = self.screen.get_rect()
        # орудие:
        self.image = pygame.image.load('gun.png')
        self.rect = self.image.get_rect()
        # позиция:
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Управляет движением пушки вдоль экрана."""
        if self.moving_up and self.y >= 0:
            self.y -= 1
        if self.moving_down and self.rect.y <= self.screen.get_height()-self.rect.height:
            self.y += 1
        self.rect.y = self.y

    def center_gun(self):
        """Центрирует пушку."""
        self.rect.midleft = self.screen_rect.midleft
        self.rect.y = self.y

    def blit(self):
        """Выводит пушку на экран."""
        self.screen.blit(self.image, self.rect)
