import sys

from pygame import init, QUIT, quit
from pygame.display import set_mode, update
from pygame.event import get
from pygame.time import Clock

from simulation.params import FRAMES_PER_SECOND, WINDOW_HEIGHT, WINDOW_WIDTH


class Simulation:
    def __init__(self) -> None:
        self.window = set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = Clock()

    def initialize_pygame_environment(self) -> None:
        init()

    def quit_game(self) -> None:
        quit()
        sys.exit()

    def check_events(self) -> None:
        for event in get():
            if event.type == QUIT:
                self.quit_game()

    def clear_window(self, background_color: tuple[int, int, int]) -> None:
        self.window.fill(background_color)

    def update_window(self) -> None:
        update()

    def make_frames_pause(self) -> None:
        self.clock.tick(FRAMES_PER_SECOND)

    def start_simulation(self, background_color: tuple[int, int, int]) -> None:
        # 3 - Инициализируем окружение pygame
        self.initialize_pygame_environment()

        while True:
            # 7 - Проверяем наличие событий и обрабатываем их
            self.check_events()

            # 9 - Очищаем окно
            self.clear_window(background_color)

            # 11 - Обновляем окно
            self.update_window()

            # 12 - Делаем паузу
            self.make_frames_pause()
