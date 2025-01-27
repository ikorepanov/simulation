import sys

import pygame

from simulation.params import BASE_PATH, FRAMES_PER_SECOND, WINDOW_WIDTH, WINDOW_HEIGHT, IMAGE_WIDTH_HEIGHT, N_PIXELS_PER_FRAME
from simulation.window import Window

import random


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

    def start_simulation(self, background_color: tuple[int, int, int], image_name: str) -> None:
        # 3 - Инициализируем окружение pygame
        self.initialize_pygame_environment()

        # 4 - Загружаем элементы: изображения, зуки и т.д.
        image = self.load_image(image_name)

        # 5 - Инициализируем переменные
        # image_x = random.randrange(0, MAX_WIDTH, IMAGE_WIDTH_HEIGHT)
        # image_y = random.randrange(0, MAX_HEIGHT, IMAGE_WIDTH_HEIGHT)
        image_rect = image.get_rect()
        MAX_WIDTH = WINDOW_WIDTH - image_rect.width
        MAX_HEIGHT = WINDOW_HEIGHT - image_rect.height
        image_rect.left = random.randrange(0, MAX_WIDTH, image_rect.width)
        image_rect.top = random.randrange(0, MAX_HEIGHT, image_rect.height)

        x_speed = N_PIXELS_PER_FRAME

        while True:
            # 7 - Проверяем наличие событий и обрабатываем их
            self.check_events()

            # 8 - Выполняем действия "в рамках фрейма"
            if (image_rect.left < 0) or (image_rect.left >= MAX_WIDTH):
                x_speed = - x_speed

            image_rect.left = image_rect.left + x_speed

            # 9 - Очищаем окно
            self.window.clear_window(background_color)

            # 10 - Рисуем все элементы окна
            self.window.draw_grid(IMAGE_WIDTH_HEIGHT)
            self.window.draw_entity(image, image_rect)

            # 11 - Обновляем окно
            self.window.update_window()

            # 12 - Делаем паузу
            self.make_frames_pause()
