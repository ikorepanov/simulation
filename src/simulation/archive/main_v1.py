# Game Loop
# I. Process input (Events)
# II. Update game
# III. Render (Draw)
# IV. Control how fast (FPS)
import sys
from pathlib import Path

import pygame
import pygwidgets

from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.rock import Rock
from simulation.entity.tree import Tree
from simulation.params import (
    BACKGROUND_COLOR,
    BLACK,
    FPS,
    GRAY,
    HEIGHT,
    IMAGE_WIDTH_HEIGHT,
    PANEL_HEIGTH,
    TITLE,
    USABLE_HEIGHT,
    WHITE,
    WIDTH,
)

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображения, зуки и т.д.
pygame.mixer.music.load(Path.cwd() / 'src/simulation/assets/sounds/watch_yourself.ogg')

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

herbivore_image = Herbivore.load_image('herbivore_small')
predator_image = Predator.load_image('predator_small')
grass_image = Grass.load_image('grass_small')
rock_image = Rock.load_image('rock_small')
tree_image = Tree.load_image('tree_small')

# 5 - Инициализируем переменные
all_sprites = pygame.sprite.Group()  # type: ignore

herbivore = Herbivore(1, herbivore_image)
predator = Predator(2, predator_image)
grass = Grass(3, grass_image)
rock = Rock(4, rock_image)
tree = Tree(5, tree_image)

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
            score_display.setValue('Score: 0')
            pygame.mixer.music.play(-1, 0.0)  # включить музыку
            playing = True
            start_button.disable()

# II. Update game
    # 8 - Выполняем действия "в рамках фрейма"
    if playing:
        all_sprites.update()
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
