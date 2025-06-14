from typing import Any

import pygame as pg
from pygame.sprite import AbstractGroup

from simulation.map import Map
from simulation.settings import BGCOLOR, DEVELOPMENT_MODE, FPS, GRIDCOLOR, HEIGHT, TILESIZE, TITLE, WIDTH


class Game:
    def __init__(self) -> None:
        # Initialize pygame, game window, etc.
        pg.init()  # initializes pygame, gets it ready to go
        pg.mixer.init()  # the mixer handles playing all the sound effects
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))  # create the window
        pg.display.set_caption(TITLE)  # "установить заголовок"
        self.clock = pg.time.Clock()  # handles the speed and keeps track of how fast we're going
        self.running = True
        self.development_mode = DEVELOPMENT_MODE

    def new(self) -> None:
        # Start a new game (reset the game, not the whole program)
        self.all_sprites: AbstractGroup[Any] = pg.sprite.Group()  # collection of sprites

        # self.player = Player(self)

        # Создадим группы для существ и препятствий
        self.creatures: AbstractGroup[Any] = pg.sprite.Group()
        self.obstacles: AbstractGroup[Any] = pg.sprite.Group()
        self.predators: AbstractGroup[Any] = pg.sprite.Group()
        self.herbivores: AbstractGroup[Any] = pg.sprite.Group()
        self.rocks: AbstractGroup[Any] = pg.sprite.Group()
        self.trees: AbstractGroup[Any] = pg.sprite.Group()
        self.grass: AbstractGroup[Any] = pg.sprite.Group()

        Map(self)

        self.run()

    def run(self) -> None:
        # NB! Game Loop
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)  # keep loop running at the right speed

    def events(self) -> None:
        # Game Loop - Events (process input)
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Check for closing window
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self) -> None:
        # Game Loop - Update
        self.all_sprites.update()

    def draw_line(self, start_pos: tuple[int, int], end_pos: tuple[int, int]) -> None:
        pg.draw.line(self.screen, GRIDCOLOR, start_pos, end_pos)

    def draw_grid(self) -> None:
        for x in range(0, WIDTH, TILESIZE):
            self.draw_line((x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            self.draw_line((0, y), (WIDTH, y))

    def draw(self) -> None:
        # Game Loop - Draw (render)
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()  # *after* drawing everything, flip the display

    def show_start_screen(self) -> None:
        # Game splash/start screen
        pass

    def show_go_screen(self) -> None:
        # Game over/continue
        pass
