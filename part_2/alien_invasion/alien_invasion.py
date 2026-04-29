import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gamestats import GameStats
from button import Button

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

# =================================== BASE ===================================
    def __init__(self):
         # подгрузка модуля настроек:
        self.settings = Settings()
        # инициализация pygame и параметров экрана:
        pygame.init()
        pygame.display.set_caption('Alien Invasion')
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                                   self.settings.screen_height))
        # создание экземпляра для записи статистики:
        self.stats = GameStats(self)
        # флаг - игра запускается в состоянии "активна":
        self.game_active = False
        # fps:
        self.clock = pygame.time.Clock()
        # модуль управления кораблем:
        self.ship = Ship(self)
        # модуль управления снарядами:
        self.bullets = pygame.sprite.Group()
        # модуль управления пришельцами:
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # создание кнопки Play:
        self.play_button = Button(self, 'Play')

# =================================== USER EVENTS ==============================
    def _check_events(self):
        """Отслеживание событий клавиатуры и мыши."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.game_active == False:
            # сбрасывает результаты прошлой игры, удаляет снаряды, пришельцев,
            # после чего создает новый флот и центрирует корабль внизу экрана:
            self.stats.reset_stats()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            # переводит игру в активное состояние:
            self.game_active = True
            # скрывает курсор мыши:
            pygame.mouse.set_visible(False)
        elif self.game_active == True:
            pass
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            

# =================================== ALIENS ===================================
    def _create_alien(self, x_pos, y_pos):
        """Создает пришельца с координатами x_pos и y_pos."""
        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.y = y_pos
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = new_alien.y
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """Создает sample пришельца и вычисляет количество пришельцев в ряду.
        Помещает столько пришельцев в ряд по x, множит эти ряды на допустимое
        количество по y."""
        sample_alien = Alien(self)
        screen_width, screen_height = self.screen.get_size()
        alien_width, alien_height = sample_alien.rect.size
        current_y = alien_height
        while current_y < (screen_height - 5 * alien_height):
            current_x = alien_width
            while current_x < (screen_width - 5 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2
            current_x = alien_width
            current_y += alien_height * 2
        current_y = alien_height

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

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте."""
        self._check_fleet_edges()
        self.aliens.update()
        # проверка столкновения пришельца с кораблем:
        if self._lose_condition():
            self._lose_ship()

    def _lose_ship(self):
        """Обрабатывает события "Корабль сбит" и прекращает игру, если кораблей
        не осталось."""
        # проверка количества жизней:
        if self.stats.ships_left >= 0:
            print(f'You have lost your ship. Ships left: {self.stats.ships_left}')
            # замораживает игру на секунду:
            sleep(1)
            # обнуляет экран:
            self.aliens.empty()
            self.bullets.empty()
            # уменьшает количество оставшихся кораблей:
            self.stats.ships_left -= 1
            # создает флот и корабль по центру низа экрана:
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.game_active = False
            print('game lost')

    def _lose_condition(self):
        """Возвращает True, если произошло сбитие корабля или пришелец достиг
        края экрана."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            return True

# =================================== BULLETS ==================================
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
        # проверка коллизий пришельцев и снарядов:
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Удаление снарядов и пришельцев, участвующих в коллизиях.
        Создание нового флота при уничтожении старого."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, 
                                                False, True)
        # уничтожение существуюших снарядов и создание нового флота
        # при условии, что первый флот уничтожен:
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

# =================================== SCREEN ===================================
    def _update_screen(self):
        """Обновление экрана и вывод всех сопутствующих вещей."""
        # при каждом проходе цикла экран заливается цветом:
        self.screen.fill(self.settings.bg_color)
        # вывод снаряда в текущей позиции корабля:
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # вывод пришельца и движение флота:
        self.aliens.draw(self.screen)
        # вывод корабля в текущей позиции:
        self.ship.blitme()
        # вывод кнопки Play, если игра неактивна:
        if not self.game_active:
            self.play_button.draw_button()
        # отображение последнего нарисованного экрана:
        pygame.display.flip()

# =================================== MAIN =====================================
    def run_game(self):
        """Запускает основной цикл игры."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()