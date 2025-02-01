from pathlib import Path

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)

WINDOW_WIDTH = 640  # pixels
WINDOW_HEIGHT = 640  # pixels (480)

PANEL_HEIGTH = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGTH

FRAMES_PER_SECOND = 30  # За каждую секунду окно перерерисовывается 30 раз (максимум)

BASE_PATH = Path(__file__).resolve().parent

IMAGE_WIDTH_HEIGHT = 80  # pixels
MAX_WIDTH = WINDOW_WIDTH - IMAGE_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - IMAGE_WIDTH_HEIGHT

N_PIXELS_PER_FRAME = 1

N_PREDATORS = 15
N_HERBIVORES = 15
