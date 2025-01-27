from pathlib import Path

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

WINDOW_WIDTH = 640  # pixels
WINDOW_HEIGHT = 480  # pixels

FRAMES_PER_SECOND = 30  # За каждую секунду окно перерерисовывается 30 раз (максимум)

BASE_PATH = Path(__file__).resolve().parent

IMAGE_WIDTH_HEIGHT = 80  # pixels
MAX_WIDTH = WINDOW_WIDTH - IMAGE_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - IMAGE_WIDTH_HEIGHT
