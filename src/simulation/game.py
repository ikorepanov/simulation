import random

import pygame as pg
from typing import NamedTuple

from simulation.entity.entity import Entity
from simulation.coordinates import Coordinates

from simulation.map import Map

from simulation.entity.tree import Tree

# from simulation.entity.grass import Grass
# from simulation.entity.herbivore import Herbivore
# from simulation.entity.predator import Predator
from simulation.entity.rock import Rock
from simulation.entity.tree import Tree
from simulation.params import BACKGROUND_COLOR, FPS, HEIGHT, MAX_NUM_OF_TILES, ROCK_NUM, TREE_NUM, TILE, TITLE, WHITE, WIDTH


from simulation.params import some_dict

class ObstacleInitParamsSet(NamedTuple):
    # x: int
    # y: int
    coordinates: Coordinates
    width: int
    height: int


class Game:
    def __init__(self) -> None:
        # Initialize game window, etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.occupied_tiles: set[tuple[int, int]] = set()

    def define_init_params(self, max_obstacle_size: int) -> ObstacleInitParamsSet:
        width_or_height = random.randrange(TILE, TILE * max_obstacle_size + 1, TILE)

        horizontal = random.choice((True, False))

        if horizontal:
            width = width_or_height
            height = TILE
            y = random.randrange(0, HEIGHT, TILE)
        else:
            width = TILE
            height = width_or_height
            y = random.randrange(0, HEIGHT - height + 1, TILE)

        x = random.randrange(0, WIDTH - width + 1, TILE)

        coordinates = Coordinates(x, y)

        # return ObstacleInitParamsSet(x, y, width, height)
        return ObstacleInitParamsSet(coordinates, width, height)

    def is_place_occupied(
        self,
        # x: int,
        # y: int,
        coordinates: Coordinates,
        width: int,
        height: int,
    ) -> bool:
        # for i in range(x, x + width + 1, TILE):
        #     for j in range(y, y + height + 1, TILE):
        #         if (i, j) in self.occupied_tiles:
        #             return True
        # return False

        x_s = []
        y_s = []

        for x in range(coordinates.x, coordinates.x + width + 1, TILE):
            x_s.append(x)
        for y in range(coordinates.y, coordinates.y + height + 1, TILE):
            y_s.append(y)
        for x in x_s:
            for y in y_s:
                if (x, y) in self.occupied_tiles:
                    return True
        return False


    def add_to_occupied_tiles_list(
        self,
        # x: int,
        # y: int,
        width: int,
        height: int,
        coordinates: Coordinates,
    ) -> None:
        # for i in range(max(0, x - TILE), min(x + width, WIDTH - TILE) + 1, TILE):
        #     for j in range(max(0, y - TILE), min(y + height, HEIGHT - TILE) + 1, TILE):
        #         self.occupied_tiles.add((i, j))

        x_s = []
        y_s = []

        for x in range(max(0, coordinates.x - TILE), min(coordinates.x + width, WIDTH - TILE) + 1, TILE):
            x_s.append(x)
        for y in range(max(0, coordinates.y - TILE), min(coordinates.y + height, HEIGHT - TILE) + 1, TILE):
            y_s.append(y)
        for x in x_s:
            for y in y_s:
                self.occupied_tiles.add((x, y))

    def spawn_obstacles(self, number_of_obstacles: int, max_obstacle_size: int, obstacle_class) -> None:
        for _ in range(number_of_obstacles):
            attempts = 0

            while attempts < 1000:
                params = self.define_init_params(max_obstacle_size)

                if self.is_place_occupied(
                    params.x,
                    params.y,
                    params.width,
                    params.height,
                ):
                    attempts += 1
                    continue

                obstacle = obstacle_class(
                    params.height,
                    params.y,
                    params.width,
                    params.height,
                )

                self.all_sprites.add(obstacle)
                self.rocks.add(obstacle)

                self.add_to_occupied_tiles_list(
                    params.height,
                    params.y,
                    params.width,
                    params.height,
                )

                break

    def new(self) -> None:
        # Start a new game
        # herbivore_image = Herbivore.load_image('herbivore_small')
        # predator_image = Predator.load_image('predator_small')
        # grass_image = Grass.load_image('grass_small')
        # tree_image = Tree.load_image('tree_small')

        map = Map()

        # self.all_sprites = pg.sprite.Group()  # type: ignore
        # self.rocks = pg.sprite.Group()  # type: ignore

        all_sprites = pg.sprite.Group()  # type: ignore
        rocks = pg.sprite.Group()  # type: ignore
        trees = pg.sprite.Group()  # type: ignore

        map.create_objects_on_map(some_dict)

        entities = map.entities.values()
        for entity in entities:
            if isinstance(entity, Rock):
                rocks.add(entity)
            elif isinstance(entity, Tree):
                trees.add(entity)
            all_sprites.add(entity)

        # self.spawn_obstacles(ROCK_NUM, MAX_NUM_OF_TILES, Rock)

        # herbivore = Herbivore(1, herbivore_image)
        # predator = Predator(2, predator_image)
        # grass = Grass(3, grass_image)
        # tree = Tree(5, tree_image)

        # self.all_sprites.add(tree, grass, herbivore, predator)

        # for _ in range(ROCK_NUM):
        #     attempts = 0
        #     while attempts < 1000:
        #         # print(attempts)
        #         # horizontal = random.choice((True, False))
        #         # print(horizontal)

        #         # if horizontal:
        #         #     width = random.randrange(TILE, TILE * MAX_NUM_OF_TILES, TILE)
        #         #     height = TILE
        #         #     y = random.randrange(0, HEIGHT, TILE)
        #         # else:
        #         #     width = TILE
        #         #     height = random.randrange(TILE, TILE * MAX_NUM_OF_TILES + 1, TILE)
        #         #     y = random.randrange(0, HEIGHT + TILE - height, TILE)

        #         # x = random.randrange(0, WIDTH - width + 1, TILE)
        #         # print(x, y, width, height)
        #         params = self.define_init_params(MAX_NUM_OF_TILES)
        #         # x = params.x
        #         # y = params.y
        #         coordinates = params.coordinates
        #         width = params.width
        #         height = params.height

        #         # if self.is_place_occupied(x, y, width, height):
        #         if self.is_place_occupied(coordinates, width, height):
        #             attempts += 1
        #             print('Занято!')
        #             continue

        #         rock = Rock(
        #             # x,
        #             # y,
        #             coordinates,
        #             width,
        #             height,
        #         )

        #         print('Создан!')

        #         self.all_sprites.add(rock)
        #         self.rocks.add(rock)

        #         print(self.all_sprites)
        #         print(self.rocks)

        #         x_s = []
        #         y_s = []

        #         for x in range(max(0, coordinates.x - TILE), min(coordinates.x + width, WIDTH - TILE) + 1, TILE):
        #             x_s.append(x)

        #         for y in range(max(0, coordinates.y - TILE), min(coordinates.y + height, HEIGHT - TILE) + 1, TILE):
        #             y_s.append(y)

        #         for x in x_s:
        #             for y in y_s:
        #                 self.occupied_tiles.add((x, y))

        #         break

        # print(self.occupied_tiles)

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
