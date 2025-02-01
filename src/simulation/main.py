import sys

import pygame
import pygwidgets

from simulation.entity.creature_mgr import CreatureMgr
from simulation.params import (
    BACKGROUND_COLOR,
    BASE_PATH,
    BLACK,
    FRAMES_PER_SECOND,
    GRAY,
    IMAGE_WIDTH_HEIGHT,
    PANEL_HEIGTH,
    USABLE_WINDOW_HEIGHT,
    WHITE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображения, зуки и т.д.
pygame.mixer.music.load(BASE_PATH + '/assets/sounds/watch_yourself.ogg')

score_display = pygwidgets.DisplayText(
    window,
    (10, USABLE_WINDOW_HEIGHT + 25),
    'Score: 0',
    textColor=BLACK,
    backgroundColor=None,
    width=140,
    fontSize=24,
)

status_display = pygwidgets.DisplayText(
    window,
    (180, USABLE_WINDOW_HEIGHT + 25),
    '',
    textColor=BLACK,
    backgroundColor=None,
    width=300,
    fontSize=24,
)

start_button = pygwidgets.TextButton(
    window,
    (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10),
    'Start',
)

# 5 - Инициализируем переменные
creature_mgr = CreatureMgr(
    window,
    WINDOW_WIDTH,
    USABLE_WINDOW_HEIGHT,
)

playing = False  # ждём, пока пользователь не нажмёт кнопку Start

# 6 - Бесконечный цикл
while True:
    # 7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_button.handleEvent(event):
            creature_mgr.start()
            score_display.setValue('Score: 0')
            pygame.mixer.music.play(-1, 0.0)  # включить музыку
            playing = True
            start_button.disable()

    # 8 - Выполняем действия "в рамках фрейма"
    if playing:
        creature_mgr.update()
        status_display.setValue('Не знаю, что тут писать...')

    # 9 - Очищаем окно
    window.fill(BACKGROUND_COLOR)

    # 10 - Рисуем все элементы окна
    def draw_grid(window: pygame.Surface, block_size: int) -> None:
        for x in range(0, WINDOW_WIDTH, block_size):
            for y in range(0, WINDOW_HEIGHT, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(window, WHITE, rect, 1)

    # 1). Рисуем сетку
    draw_grid(window, IMAGE_WIDTH_HEIGHT)

    # 2). С помощью менеджера рисуем существ
    if playing:
        creature_mgr.draw()

    # 3). Изображаем нижнюю панель с данными состояния и кнопкой Start
    pygame.draw.rect(
        window,
        GRAY,
        pygame.Rect(
            0,
            USABLE_WINDOW_HEIGHT,
            WINDOW_WIDTH,
            PANEL_HEIGTH,
        ),
    )
    score_display.draw()
    status_display.draw()
    start_button.draw()

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)  # ожидание pygame
