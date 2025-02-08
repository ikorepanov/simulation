# Game Loop
# I. Process input (Events)
# II. Update game
# III. Render (Draw)
# IV. Control how fast (FPS)

# 1 - Импортируем пакеты
import sys
from pathlib import Path

import pygame as pg
import pygwidgets

from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.rock import Rock
from simulation.entity.tree import Tree

# 2 - Определяем константы
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


class Game:
    def __init__(self) -> None:
        # 3 - Инициализируем окружение pygame
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        self.playing = False  # ждём, пока пользователь не нажмёт кнопку Start

        # 4 - Загружаем элементы: изображения, зуки и т.д.
        pg.mixer.music.load(Path.cwd() / 'src/simulation/assets/sounds/watch_yourself.ogg')

        self.score_display = pygwidgets.DisplayText(
            self.window,
            (10, USABLE_HEIGHT + 25),
            'Score: 0',
            textColor=BLACK,
            backgroundColor=None,
            width=140,
            fontSize=24,
        )

        self.status_display = pygwidgets.DisplayText(
            self.window,
            (180, USABLE_HEIGHT + 25),
            '',
            textColor=BLACK,
            backgroundColor=None,
            width=300,
            fontSize=24,
        )

        self.start_button = pygwidgets.TextButton(
            self.window,
            (WIDTH - 110, USABLE_HEIGHT + 10),
            'Start',
        )

        herbivore_image = Herbivore.load_image('herbivore_small')
        predator_image = Predator.load_image('predator_small')
        grass_image = Grass.load_image('grass_small')
        rock_image = Rock.load_image('rock_small')
        tree_image = Tree.load_image('tree_small')

        # 5 - Инициализируем переменные
        self.all_sprites = pg.sprite.Group()  # type: ignore

        herbivore = Herbivore(1, herbivore_image)
        predator = Predator(2, predator_image)
        grass = Grass(3, grass_image)
        rock = Rock(4, rock_image)
        tree = Tree(5, tree_image)

        self.all_sprites.add(tree, grass, rock, herbivore, predator)

    def events(self) -> None:
        # 7 - Проверяем наличие событий и обрабатываем их
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.show_go_screen()
                pg.quit()
                sys.exit()

            if self.start_button.handleEvent(event):
                self.score_display.setValue('Score: 0')
                pg.mixer.music.play(-1, 0.0)  # включить музыку
                self.playing = True
                self.start_button.disable()

    def update(self) -> None:
        # 8 - Выполняем действия "в рамках фрейма"
        if self.playing:
            self.all_sprites.update()
            self.status_display.setValue('Не знаю, что тут писать...')

    def draw(self) -> None:
        # 9 - Очищаем окно
        self.window.fill(BACKGROUND_COLOR)

        # 10 - Рисуем все элементы окна
        def draw_grid(window: pg.Surface, block_size: int) -> None:
            for x in range(0, WIDTH, block_size):
                for y in range(0, USABLE_HEIGHT, block_size):
                    rect = pg.Rect(x, y, block_size, block_size)
                    pg.draw.rect(window, WHITE, rect, 1)

        # 1). Рисуем сетку
        draw_grid(self.window, IMAGE_WIDTH_HEIGHT)

        # 2). С помощью менеджера рисуем существ
        if self.playing:
            self.all_sprites.draw(self.window)

        # 3). Изображаем нижнюю панель с данными состояния и кнопкой Start
        pg.draw.rect(
            self.window,
            GRAY,
            pg.Rect(
                0,
                USABLE_HEIGHT,
                WIDTH,
                PANEL_HEIGTH,
            ),
        )
        self.score_display.draw()
        self.status_display.draw()
        self.start_button.draw()

        # 11 - Обновляем окно
        # *after* drawing everything:
        pg.display.update()  # Также, можно pygame.display.flip()

    def run(self) -> None:
        # 6 - Бесконечный цикл (Game Loop)
        while True:
            # I. Process input (Events)
            self.events()
            # II. Update game
            self.update()
            # III. Render (Draw)
            self.draw()
            # IV. Control how fast (FPS): keep loop running at the right speed
            # 12 - Делаем паузу
            self.clock.tick(FPS)

    def show_start_screen(self) -> None:
        print('Игра началась')

    def show_go_screen(self) -> None:
        print('Игра закончилась')
