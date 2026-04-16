# 12.5. Клавиши.
# Создайте файл Pygame, который создает пустой экран. В цикле событий выводите
# значение атрибута event.key при обнаружении события pyga­me.KEYDOWN.
# Запустите программу, нажимайте различные клавиши и понаблюдайте за
# реакцией Pygame.

import sys
import pygame

class Exercise:
    """"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (120, 120, 120)
        self.clock = pygame.time.Clock()
        self.fps = 60
        pygame.display.set_caption('Упражнение 12.5. Клавиши.')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print(f'Нажата клавиша {event.key} ({pygame.key.name(event.key)}).\nВыход.')
                    sys.exit()
                else:
                    print(f'Нажата клавиша {event.key} ({pygame.key.name(event.key)})')

    def run_exercise(self):
        while True:
            self.check_events()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(self.fps)
        
ekz = Exercise()
ekz.run_exercise()