import random
from abc import abstractmethod

import pygame

from simulation.entity.entity import Entity
from simulation.params import BASE_PATH
from simulation.window import Window


class Creature(Entity):
    def __init__(
        self,
        window: Window,
        window_width: int,
        window_height: int,
        image_name: str,
    ):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        path_to_image = str(BASE_PATH) + f'/assets/images/{image_name}.png'
        self.image = pygame.image.load(path_to_image)

        creature_rect = self.image.get_rect()
        self.width = creature_rect.width
        self.height = creature_rect.height
        self.max_width = window_width - self.width
        self.max_height = window_height - self.height

        # выбираем произвольную начальную позицию
        self.x = random.randrange(0, self.max_width, self.width)
        self.y = random.randrange(0, self.max_height, self.height)

        # выбираем произвольную скорость между -3 и 3, но не ноль
        speed_list = [-3, -2, -1, 1, 2, 3]
        self.x_speed = random.choice(speed_list)

    def update(self) -> None:
        if (self.x < 0) or (self.x >= self.max_width):
            self.x_speed = - self.x_speed

        self.x = self.x + self.x_speed

    def draw(self) -> None:
        self.window.draw_entity(self.image, self.x, self.y)

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
