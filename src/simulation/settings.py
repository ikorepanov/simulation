# define colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
PURPLE = (128, 0, 128)

# game options/settings
TITLE = 'Simulation'
WIDTH = 400  # 1024
HEIGHT = 300  # 768
FPS = 30  # 60  # How many times per second does the game loop repeat?
BGCOLOR = DARKGREY
GRIDCOLOR = LIGHTGREY

TILESIZE = 100  # 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# finding free tile
NUMBER_OF_ATTEMPTS = 1000

# entities settings
ATTACK_POWER = 100
AMOUNT_OF_GRASS = 100
VELOCITY = 100
HP = 100

# number of entities
PREDATOR_NUMBER = 1
HERBIVORE_NUMBER = 1
ROCK_NUMBER = 0
TREE_NUMBER = 0
GRASS_NUMBER = 0
