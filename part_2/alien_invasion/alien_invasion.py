import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption('Alien Invasion')

    def _check_events(self):
        """Отслеживание событий клавиатуры и мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit

    def _update_screen(self):
        # при каждом проходе цикла экран заливается цветом:
        self.screen.fill(self.settings.bg_color)
        # вывод корабля в текущей позиции:
        self.ship.blitme()
        # отображение последнего нарисованного экрана:
        pygame.display.flip()
        self.clock.tick(60)

    def run_game(self):
        """Запускает основной цикл игры."""
        while True:
            self._check_events()
            self._update_screen()

if __name__ == '__main__':
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()