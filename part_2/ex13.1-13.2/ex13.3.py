import pygame
import sys
from pygame.sprite import Sprite
from random import randint

class Exercise:
    """Основной класс упражнения."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Exercise 13.1 - Stars')
        self.bg_color = (15, 15, 15)

        self.stars = pygame.sprite.Group()
        self._create_star_net()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()


    def _create_new_star(self, x_pos, y_pos):
        new_star = Star(self)
        new_star.x = x_pos
        new_star.rect.x = new_star.x
        new_star.rect.y = y_pos
        self.stars.add(new_star)


    def _create_star_net(self):
        sample_star = Star(self)
        star_width = sample_star.rect.width
        star_height = sample_star.rect.height

        screen_width, screen_height = self.screen.get_size()

        current_x = star_width
        current_y = star_height
        while current_y < (screen_height - star_height):
            while current_x < (screen_width - star_width):
                offset_x = randint(-10, 10)
                offset_y = randint(-10, 10)
                self._create_new_star(current_x + offset_x, current_y + offset_y)
                current_x += star_width
            current_y += star_height
            current_x = star_width
        current_y = star_height
        print(f'Создано звезд: {len(self.stars)}')


    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)


    def run_exercise(self):
        while True:
            self._check_events()
            self.update_screen()


class Star(Sprite):
    """Класс звезды."""

    def __init__(self, exercise):
        super().__init__()
        self.screen = exercise.screen

        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


if __name__ == '__main__':
    rr = Exercise()
    rr.run_exercise()