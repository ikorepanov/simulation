# game options/settings
WIDTH = 4
HEIGHT = 3
DEVELOPMENT_MODE = True

TILESIZE = 100  # 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# finding free tile
NUMBER_OF_ATTEMPTS = 1000

# entities settings
ATTACK_POWER = 100
AMOUNT_OF_GRASS = 100
PREDATOR_SPEED = 1
PREDATOR_HP = 100
HERBIVORE_SPEED = 1
HERBIVORE_HP = 100

# number of entities
PREDATOR_NUMBER = 0
HERBIVORE_NUMBER = 1
ROCK_NUMBER = 0
TREE_NUMBER = 0
GRASS_NUMBER = 2

# ANSI
ESC = '\033['  # Начало ANSI escape-последовательности
BACKGROUND_256 = '48;5;'  # Установить цвет фона; использовать 256-цветный режим
ANSI_RESET = '\033[0'
ANSI_STYLE_END = 'm'  # Завершить escape-команду и применить стили (конец описания стиля)

# sprites
HERBIVORE = '\U0001F411 '
GRASS = '\U0001F33F '
PREDATOR = '\U0001F43A '
ROCK = '\U0001FAA8  '
TREE = '\U0001F333 '
EMPTY_TILE = '   '

# current color scheme: industrial, midnight, ocean, forest, twilight, glacier, abyss
COLOR_SCHEME = 'abyss'
