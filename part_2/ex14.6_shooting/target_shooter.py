import pygame
import sys

from pygame import time
from pygame.sprite import Sprite

from bullet import Bullet
from gun import Gun

class TargetShooting:
    """Основной класс упражнения "Стрельба по мишени"."""

# ================================= BASE =======================================
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Target Shooting Exercise')
        self.bg_color = (120, 120, 120)
        self.gun = Gun(self)
        self.bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.gun.blit()
        pygame.display.flip()

    def run_gun(self):
        while True:
            self.check_user_events()
            self._update_screen()
            self.bullet.update()
            self.gun.update()
            self.clock.tick(60)

# ================================= USER EVENTS ================================
    def check_user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.gun.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.gun.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = False

# ================================= TARGET =====================================
# ================================= BULLETS ====================================
    def _fire_bullet(self):
        """Создает новый снаряд и добавляет его в группу bullets."""
        new_bullet = self.bullet
        self.bullets.add(new_bullet)

    def _bullets_update(self):
        self.bullet.update()

# ================================= SETTINGS ===================================
# ================================= SCREEN =====================================
# ================================= GUN ========================================
# ================================= MAIN =======================================
if __name__ == '__main__':
    rr = TargetShooting()
    rr.run_gun()