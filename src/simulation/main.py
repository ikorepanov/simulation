# Game Loop
# I. Process input (Events)
# II. Update game
# III. Render (Draw)
# IV. Control how fast (FPS)

import sys

import pygame
import pygwidgets

# from simulation.entity.creature_mgr import CreatureMgr
from simulation.params import (
    BACKGROUND_COLOR,
    BASE_PATH,
    BLACK,
    FPS,
    GRAY,
    IMAGE_WIDTH_HEIGHT,
    PANEL_HEIGTH,
    USABLE_HEIGHT,
    WHITE,
    HEIGHT,
    WIDTH,
)

from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.grass import Grass
from simulation.entity.rock import Rock
from simulation.entity.tree import Tree

# 3 - Инициализируем окружение pygame
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simulation')
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображения, зуки и т.д.
pygame.mixer.music.load(BASE_PATH + '/assets/sounds/watch_yourself.ogg')

score_display = pygwidgets.DisplayText(
    window,
    (10, USABLE_HEIGHT + 25),
    'Score: 0',
    textColor=BLACK,
    backgroundColor=None,
    width=140,
    fontSize=24,
)

status_display = pygwidgets.DisplayText(
    window,
    (180, USABLE_HEIGHT + 25),
    '',
    textColor=BLACK,
    backgroundColor=None,
    width=300,
    fontSize=24,
)

start_button = pygwidgets.TextButton(
    window,
    (WIDTH - 110, USABLE_HEIGHT + 10),
    'Start',
)

# 5 - Инициализируем переменные
# creature_mgr = CreatureMgr(
#     window,
#     WIDTH,
#     USABLE_WINDOW_HEIGHT,
# )

all_sprites = pygame.sprite.Group()
herbivore = Herbivore(1)
predator = Predator(2)
grass = Grass(3)
rock = Rock(4)
tree = Tree(5)
all_sprites.add(tree, grass, rock, herbivore, predator)

playing = False  # ждём, пока пользователь не нажмёт кнопку Start

# 6 - Бесконечный цикл (Game Loop)
while True:
    # I. Process input (Events)
    # 7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_button.handleEvent(event):
            # creature_mgr.start()
            score_display.setValue('Score: 0')
            pygame.mixer.music.play(-1, 0.0)  # включить музыку
            playing = True
            start_button.disable()

# II. Update game
    # 8 - Выполняем действия "в рамках фрейма"
    if playing:
        all_sprites.update()
        # creature_mgr.update()  # NB! Удалить
        status_display.setValue('Не знаю, что тут писать...')

# III. Render (Draw)
    # 9 - Очищаем окно
    window.fill(BACKGROUND_COLOR)

    # 10 - Рисуем все элементы окна
    def draw_grid(window: pygame.Surface, block_size: int) -> None:
        for x in range(0, WIDTH, block_size):
            for y in range(0, USABLE_HEIGHT, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(window, WHITE, rect, 1)

    # 1). Рисуем сетку
    draw_grid(window, IMAGE_WIDTH_HEIGHT)

    # 2). С помощью менеджера рисуем существ
    if playing:
        all_sprites.draw(window)
        # creature_mgr.draw()  # NB! Удалить

    # 3). Изображаем нижнюю панель с данными состояния и кнопкой Start
    pygame.draw.rect(
        window,
        GRAY,
        pygame.Rect(
            0,
            USABLE_HEIGHT,
            WIDTH,
            PANEL_HEIGTH,
        ),
    )
    score_display.draw()
    status_display.draw()
    start_button.draw()

    # 11 - Обновляем окно
    # *after* drawing everything:
    pygame.display.update()  # Также, можно pygame.display.flip()

# IV. Control how fast (FPS): keep loop running at the right speed
    # 12 - Делаем паузу
    clock.tick(FPS)  # ожидание pygame
