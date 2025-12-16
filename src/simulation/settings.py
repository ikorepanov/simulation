# game options/settings
WIDTH = 40
HEIGHT = 20
DELAY_DURATION = 1

# finding free coord
NUMBER_OF_ATTEMPTS = 1000

# entities settings
MIN_ATTACK_POWER = 1
MAX_ATTACK_POWER = MIN_ATTACK_POWER + 2
MIN_GRASS_HEIGHT = 3
MAX_GRASS_HEIGHT = MIN_GRASS_HEIGHT + 5
MIN_HERBIVORE_HP = 4
MAX_HERBIVORE_HP = MIN_HERBIVORE_HP + 2
PREDATOR_HP = 100
MIN_PREDATOR_SPEED = 1
MAX_PREDATOR_SPEED = MIN_PREDATOR_SPEED + 2
MIN_HERBIVORE_SPEED = 2
MAX_HERBIVORE_SPEED = MIN_HERBIVORE_SPEED + 2

# number of entities
PREDATOR_NUMBER = 10
HERBIVORE_NUMBER = 50
ROCK_NUMBER = 50
TREE_NUMBER = 50
GRASS_NUMBER = 200

# ANSI
ANSI_ESC = '\033'  # Начало ANSI escape-последовательности
ANSI_BACKGROUND_256 = '[48;5;'  # Установить цвет фона; использовать 256-цветный режим
ANSI_RESET = '[0'
ANSI_BEGINNING_PREV_LINE = '[F'
ANSI_CLEAR_LINE = '[K'
ANSI_STYLE_END = (
    'm'  # Завершить escape-команду и применить стили (конец описания стиля)
)

# sprites
HERBIVORE_SPRITE = '\U0001f411 '
GRASS_SPRITE = '\U0001f33f '
PREDATOR_SPRITE = '\U0001f43a '
ROCK_SPRITE = '\U0001faa8  '
TREE_SPRITE = '\U0001f333 '
EMPTY_COORD_SPRITE = '   '

# current color scheme: industrial, midnight, ocean, forest, twilight, glacier, abyss
COLOR_SCHEME = 'abyss'
