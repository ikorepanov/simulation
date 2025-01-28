import sys

import pygame

from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.params import (
    BASE_PATH,
    FRAMES_PER_SECOND,
    IMAGE_WIDTH_HEIGHT,
    N_HERBIVORES,
    N_PREDATORS,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
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

    def load_sound(self, sound_name: str) -> None:
        path_to_sound = str(BASE_PATH) + f'/assets/sounds/{sound_name}.ogg'
        pygame.mixer.music.load(path_to_sound)

    def play_sound(self) -> None:
        pygame.mixer.music.play(-1, 0.0)

    def start_simulation(self, background_color: tuple[int, int, int], sound_name: str) -> None:
        # 3 - Инициализируем окружение pygame
        self.initialize_pygame_environment()

        # 4 - Загружаем элементы: изображения, зуки и т.д.
        self.load_sound(sound_name)
        # self.play_sound()

        # 5 - Инициализируем переменные
        predator_list = []
        herbivore_list = []

        for predator in range(0, N_PREDATORS):
            predator = Predator(self.window, WINDOW_WIDTH, WINDOW_HEIGHT, 'predator_small')
            predator_list.append(predator)

        for herbivore in range(0, N_HERBIVORES):
            herbivore = Herbivore(self.window, WINDOW_WIDTH, WINDOW_HEIGHT, 'herbivore_small')
            herbivore_list.append(herbivore)

        while True:
            # 7 - Проверяем наличие событий и обрабатываем их
            self.check_events()

            # 8 - Выполняем действия "в рамках фрейма"
            for predator in predator_list:
                predator.update()

            for herbivore in herbivore_list:
                herbivore.update()

            # 9 - Очищаем окно
            self.window.clear_window(background_color)

            # 10 - Рисуем все элементы окна
            self.window.draw_grid(IMAGE_WIDTH_HEIGHT)

            for predator in predator_list:
                predator.draw()

            for herbivore in herbivore_list:
                herbivore.draw()

            # 11 - Обновляем окно
            self.window.update_window()

            # 12 - Делаем паузу
            self.make_frames_pause()
