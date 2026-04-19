import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
         # подгружаем модуль настроек:
        self.settings = Settings()

        # инициализируем pygame и параметры экрана:
        pygame.init()
        pygame.display.set_caption('Alien Invasion')
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # fps:
        self.clock = pygame.time.Clock()
        # модуль управления кораблем:
        self.ship = Ship(self)
        # модуль управления снарядами:
        self.bullets = pygame.sprite.Group()
        # модуль управления пришельцами:
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def _check_events(self):
        """Отслеживание событий клавиатуры и мыши."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Отслеживает нажатие клавиш."""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Отслеживает отпускание клавиш."""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


    def _create_alien(self, alien_number, row_number):
        """Создаем пришельца и размещает его во флот."""
        new_alien = Alien(self)
        alien_width, alien_height = new_alien.rect.size

        # позиция по x: отступ + номер столбца х шаг (2 ширины пришельца)
        new_alien.x = alien_width + 2 * alien_width * alien_number
        new_alien.rect.x = new_alien.x

        # позиция по y: отступ сверху + номер строки х шаг (2 высоты пришельца)
        new_alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(new_alien)


    def _create_fleet(self):
        """Создает пришельца и вычисляет количество пришельцев в ряду."""
        # получаем актуальные размеры экрана:
        screen_width, screen_height = self.screen.get_size()

        # создаем первого пришельца для измерения размеров:
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # вычисляем доступное пространство:
        available_space_x = screen_width - 2 * alien_width
        available_space_y = screen_height - 3 * alien_height

        # кол-во пришельцев по горизонтали и вертикали:
        number_aliens_x = available_space_x // (2 * alien_width)
        number_rows = available_space_y // (2 * alien_height)

        # создаем флот - строки и столбцы пришельцев:
        for row_number in range(number_rows):
            for alien_number in range (number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _fire_bullet(self):
        """Создает новый снаряд и добавляет его в группу bullets."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # обновление позиции снарядом:
        self.bullets.update()
        # удаление снарядов, вышедших за край экрана:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление его движения."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1        


    def _update_screen(self):
        """Обновление экрана и вывод всех сопутствующих вещей."""
        # при каждом проходе цикла экран заливается цветом:
        self.screen.fill(self.settings.bg_color)

        # вывод снаряда в текущей позиции корабля:
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # вывод пришельца и движение флота:
        self.aliens.draw(self.screen)
        self._update_aliens()

        # вывод корабля в текущей позиции:
        self.ship.blitme()

        # отображение последнего нарисованного экрана:
        pygame.display.flip()


    def run_game(self):
        """Запускает основной цикл игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()