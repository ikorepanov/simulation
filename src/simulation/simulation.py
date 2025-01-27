import sys

import pygame

from simulation.params import BASE_PATH, FRAMES_PER_SECOND
from simulation.window import Window


class Simulation:
    def __init__(self) -> None:
        self.window = Window()
        self.clock = pygame.time.Clock()

    def initialize_pygame_environment(self) -> None:
        pygame.init()

    def quit_game(self) -> None:
        pygame.quit()
        sys.exit()

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

    def make_frames_pause(self) -> None:
        self.clock.tick(FRAMES_PER_SECOND)

    def load_image(self, image_name: str) -> pygame.surface.Surface:
        path_to_image = str(BASE_PATH) + f'/assets/images/{image_name}.png'
        return pygame.image.load(path_to_image)

    def start_simulation(self, background_color: tuple[int, int, int], image_name: str, x: int, y: int) -> None:
        # 3 - Инициализируем окружение pygame
        self.initialize_pygame_environment()

        # 4 - Загружаем элементы: изображения, зуки и т.д.
        image = self.load_image(image_name)

        while True:
            # 7 - Проверяем наличие событий и обрабатываем их
            self.check_events()

            # 9 - Очищаем окно
            self.window.clear_window(background_color)

            # 10 - Рисуем все элементы окна
            self.window.draw_entity(image, x, y)

            # 11 - Обновляем окно
            self.window.update_window()

            # 12 - Делаем паузу
            self.make_frames_pause()
