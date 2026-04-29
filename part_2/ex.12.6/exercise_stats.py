class ExerciseStats:
    """Отвечает за статистику упражнения (игры)."""

    def __init__(self):
        """Инициализирует статистику."""
        self.start_stats()

    def start_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.hitted_aliens = []
        self.ships_lost = 0