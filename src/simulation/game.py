import pygame as pg

from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.rock import Rock
from simulation.entity.tree import Tree
from simulation.params import BACKGROUND_COLOR, FPS, HEIGHT, IMAGE_WIDTH_HEIGHT, TITLE, USABLE_HEIGHT, WHITE, WIDTH


class Game:
    def __init__(self) -> None:
        pg.init()
        pg.mixer.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self) -> None:
        herbivore_image = Herbivore.load_image('herbivore_small')
        predator_image = Predator.load_image('predator_small')
        grass_image = Grass.load_image('grass_small')
        rock_image = Rock.load_image('rock_small')
        tree_image = Tree.load_image('tree_small')

        self.all_sprites = pg.sprite.Group()  # type: ignore

        herbivore = Herbivore(1, herbivore_image)
        predator = Predator(2, predator_image)
        grass = Grass(3, grass_image)
        rock = Rock(4, rock_image)
        tree = Tree(5, tree_image)

        self.all_sprites.add(tree, grass, rock, herbivore, predator)

        self.run()

    def run(self) -> None:
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def update(self) -> None:
        self.all_sprites.update()

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self) -> None:
        self.window.fill(BACKGROUND_COLOR)

        def draw_grid(window: pg.Surface, block_size: int) -> None:
            for x in range(0, WIDTH, block_size):
                for y in range(0, USABLE_HEIGHT, block_size):
                    rect = pg.Rect(x, y, block_size, block_size)
                    pg.draw.rect(window, WHITE, rect, 1)

        draw_grid(self.window, IMAGE_WIDTH_HEIGHT)

        self.all_sprites.draw(self.window)

        pg.display.flip()

    def show_start_screen(self) -> None:
        print('Игра началась')

    def show_go_screen(self) -> None:
        print('Игра закончилась')
