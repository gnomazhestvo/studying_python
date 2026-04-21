import pygame
import sys

from pygame.sprite import Sprite
from random import randint

class Exercise:
    """Основной класс управления упражнением."""

    def __init__(self):
        """Инициализация экрана и параметров."""
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Exercise 13.3, 13.4 - Raindrops')
        self.bg_color = (80, 80, 80)
        self.clock = pygame.time.Clock()
        self.drop = Drop(self)
        self.drops = pygame.sprite.Group()
        self._create_rain()

    def _check_events(self):
        """Обработка событий от пользователя."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    

    def _create_one_drop(self, x_pos, y_pos):
        """Создание капли и добавление ее в группу капель."""
        new_drop = Drop(self)
        new_drop.x = x_pos
        new_drop.y = y_pos
        new_drop.rect.x = new_drop.x
        new_drop.rect.y = new_drop.y
        self.drops.add(new_drop)

    def _create_rain(self):
        """Создает сетку из капель."""
        # создание капли для определения размеров:
        sample_drop = Drop(self)
        drop_width, drop_height = sample_drop.rect.size
        # определяем размеры экрана, чтобы определить его вместимость:
        screen_width, screen_height = self.screen.get_size()
        # создаем капли - сначала в правом верхнем углу, далее по циклам:
        current_y = drop_height
        while current_y < (screen_height - drop_height):
            current_x = drop_width
            while current_x < (screen_width - drop_width):
                self._create_one_drop(current_x, current_y)
                current_x += drop_width
            current_x = drop_width
            current_y += drop_height
        current_y = drop_height

    def _create_new_row(self):
        """Создает новый ряд капель сверху."""
        sample_drop = Drop(self)
        drop_width, drop_height = sample_drop.rect.size
        screen_width = self.screen.get_width()
        current_y = drop_height
        current_x = drop_width
        while current_x < (screen_width - drop_width):
            self._create_one_drop(current_x, current_y)
            current_x += drop_width
        current_x = drop_width

    def _count_drops_per_row(self):
        """Возвращает количество капель на каждый ряд."""
        sample_drop = Drop(self)
        drop_width = sample_drop.rect.width
        screen_width = self.screen.get_width()
        drops_per_row = (screen_width - drop_width) // drop_width
        return drops_per_row

    def _remove_lowest_drops_row(self):
        """Удаляет ряд капель, которые вышли за нижний край экрана и создает новый ряд сверху, когда это произошло."""
        removed_count = 0
        for drop in self.drops.copy():
            if drop.rect.top >= self.screen.get_height():
                self.drops.remove(drop)
                removed_count += 1
                if removed_count == self._count_drops_per_row():
                    self._create_new_row()
                
    def _update_drops(self):
        """Перемещение капель - из модуля drop."""
        self._remove_lowest_drops_row()
        self.drops.update()


    def _update_screen(self):
        """Вывод изображения."""
        self.screen.fill(self.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()

    def run_exercise(self):
        """Основной метод упражнения."""
        while True:
            self._update_screen()
            self._update_drops()
            self.clock.tick(60)
            self._check_events()


class Drop(Sprite):
    """Класс управления каплями (звездами)."""

    def __init__(self, exercise):
        """Инициализация."""
        super().__init__()
        self.screen = exercise.screen
        self.screen_rect = exercise.screen.get_rect()
        # загрузка изображения:
        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.direction = 1

        # каждая новая капля появляется в левом верхнем углу экрана,
        # удаленная от левого края на ширину капли, и удаленная от
        # верха экрана на высоту капли:
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции капли:
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение капли."""
        self.y += self.speed * self.direction
        self.rect.y = self.y

    def check_edge(self):
        """Возвращает True, если капля достигает нижнего края экрана."""
        return self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0


if __name__ == '__main__':
    rr = Exercise()
    rr.run_exercise()