class Settings:
    """Класс для хранения настроек игры."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.full_screen = False
        self.bg_color = (230, 230, 230)

        # параметры корабля:
        self.ship_speed = 1.5

        # параметры снаряда:
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # параметры пришельцев:
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # величина снижения флота при достижении им края
        self.fleet_direction = 1 # -1 будет обозначать обратное направление