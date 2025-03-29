from simulation.entity.rock import Rock
from simulation.entity.tree import Tree


GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
BLUE = (0, 0, 255)

WIDTH = 640  # pixels
HEIGHT = 480  # pixels
PANEL_HEIGTH = 60  # pixels
USABLE_HEIGHT = HEIGHT - PANEL_HEIGTH

FPS = 30  # За каждую секунду окно перерерисовывается 30 раз (максимум)

IMAGE_WIDTH_HEIGHT = 80  # pixels
MAX_WIDTH = WIDTH - IMAGE_WIDTH_HEIGHT
MAX_HEIGHT = HEIGHT - IMAGE_WIDTH_HEIGHT

N_PIXELS_PER_FRAME = 1

N_PREDATORS = 3
N_HERBIVORES = 3
N_GRASS = 3

TITLE = 'Simulation'

ROCK_NUM = 1
TREE_NUM = 2
MAX_NUM_OF_TILES = 4

TILE = 40  # pixels

some_dict = {
    Rock: ROCK_NUM,
    Tree: TREE_NUM,
}
