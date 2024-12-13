# 1 - Импортируем пакеты
import sys

import pygame

from simulation.entities.herbivore import Herbivore
from simulation.entities.predator import Predator


def draw_grid(block_size: int) -> None:
    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range(0, WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(window, WHITE, rect, 1)


# 2 - Определяем константы
BLUE = (0, 0, 255)
WHITE = (200, 200, 200)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BLOCK_SIZE = 80  # Set the size of the grid block

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. - Загружаем элементы: изображения, звуки и т.д.

# 5. - Инициализируем переменные
o_herbivore = Herbivore(window, 80, 80, 0, 0)
o_predator = Predator(window, 320, 320, 0, 0, 0)

# 6. - Бесконечный цикл: здесь мы начинаем основной цикл
while True:

    # 7. - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        # Нажата кнопка "закрыть"? Выходим из pygame и завершаем программу
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. - Выполняем действия "в рамках фрейма"

    # 9. - Очищаем окно
    window.fill(BLUE)

    # 10. - Рисуем все элементы окна
    o_herbivore.draw()
    o_predator.draw()

    draw_grid(BLOCK_SIZE)

    # 11. - Обновляем окно
    pygame.display.update()

    # 12. - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)
