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

    def _create_row(self, y):
        """Создает ряд из капель."""
        # создание капли для определения размеров:
        sample_drop = Drop(self)
        drop_width = sample_drop.rect.width
        # определяем размеры экрана, чтобы определить его вместимость:
        screen_width = self.screen.get_width()
        # создаем капли - сначала в правом верхнем углу, далее по циклу:
        current_x = drop_width
        while current_x < (screen_width - drop_width):
            offset_x = randint(-10, 10)
            offset_y = randint(-10, 10)
            self._create_one_drop(current_x+offset_x, y+offset_y)
            current_x += drop_width
        current_x = drop_width

    def _create_rain(self):
        """Множит ряды по оси y. Работает аналогично _create_row()"""
        sample_drop = Drop(self)
        drop_height = sample_drop.rect.height
        screen_height = self.screen.get_height()

        current_y = drop_height
        while current_y < (screen_height - drop_height):
            self._create_row(current_y)
            current_y += drop_height
        current_y = drop_height

    def _remove_bottom_row(self):
        """Удаляет ряд капель, которые достигли нижнего края."""
        # найдем максимальный y:
        for drop in self.drops.copy():
            if drop.rect.top > self.screen.get_height():
                self.drops.remove(drop)

    def _add_new_row(self):
        """Добавляет новый ряд капель за верхним краем экрана."""
        sample_drop = Drop(self)
        drop_height = sample_drop.rect.height
        new_y = -drop_height
        self._create_row(new_y)

    def _update_drops(self):
        """Перемещение капель - из модуля drop."""
        self._check_drops_edge()
        self.drops.update()

    def _check_drops_edge(self):
        """Когда нижний ряд достигает края экрана, создается новый ряд."""
        for drop in self.drops.copy():
            if drop.check_edge():
                self._remove_bottom_row()
                self._add_new_row()
                break


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
        self.y += 0.3
        self.rect.y = self.y

    def check_edge(self):
        """Возвращает True, если капля достигает нижнего края экрана."""
        return self.rect.bottom >= self.screen_rect.bottom


if __name__ == '__main__':
    rr = Exercise()
    rr.run_exercise()