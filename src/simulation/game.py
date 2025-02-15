import random

import pygame as pg

from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.rock import Rock
from simulation.entity.tree import Tree
from simulation.params import BACKGROUND_COLOR, FPS, HEIGHT, MAX_NUM_OF_TILES, ROCK_NUM, TILE, TITLE, WHITE, WIDTH


class Game:
    def __init__(self) -> None:
        # Initialize game window, etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self) -> None:
        # Start a new game
        herbivore_image = Herbivore.load_image('herbivore_small')
        predator_image = Predator.load_image('predator_small')
        grass_image = Grass.load_image('grass_small')
        tree_image = Tree.load_image('tree_small')

        self.all_sprites = pg.sprite.Group()  # type: ignore
        self.rocks = pg.sprite.Group()  # type: ignore

        herbivore = Herbivore(1, herbivore_image)
        predator = Predator(2, predator_image)
        grass = Grass(3, grass_image)
        tree = Tree(5, tree_image)

        self.all_sprites.add(tree, grass, herbivore, predator)

        for _ in range(ROCK_NUM):
            orientation = random.choice(['horizontal', 'vertical'])

            if orientation == 'horizontal':
                width = random.randrange(TILE, TILE * MAX_NUM_OF_TILES, TILE)
                height = TILE
                y = random.randrange(0, HEIGHT, TILE)
            else:
                width = TILE
                height = random.randrange(TILE, TILE * MAX_NUM_OF_TILES, TILE)
                y = random.randrange(0, HEIGHT + TILE - height, TILE)

            rock = Rock(
                random.randrange(0, WIDTH - width, TILE),
                y,
                width,
                height,
            )

            self.all_sprites.add(rock)
            self.rocks.add(rock)

        self.run()

    def run(self) -> None:
        # Game Loop
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def update(self) -> None:
        # Game Loop - Update
        self.all_sprites.update()

    def events(self) -> None:
        # Game Loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw_grid(self, screen: pg.Surface, block_size: int) -> None:
        for x in range(0, WIDTH, block_size):
            for y in range(0, HEIGHT, block_size):
                rect = pg.Rect(x, y, block_size, block_size)
                pg.draw.rect(screen, WHITE, rect, 1)

    def draw(self) -> None:
        # Game Loop - draw
        self.screen.fill(BACKGROUND_COLOR)

        self.draw_grid(self.screen, TILE)

        self.all_sprites.draw(self.screen)

        # *after* drawing everythin, flip the display
        pg.display.flip()

    def show_start_screen(self) -> None:
        # Game splash/start screen
        print('Игра началась')

    def show_go_screen(self) -> None:
        # Game over/continue
        print('Игра закончилась')
