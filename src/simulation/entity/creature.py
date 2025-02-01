import random
from abc import abstractmethod

import pygame
import pygwidgets

from simulation.entity.entity import Entity


class Creature(Entity):
    @abstractmethod
    def __init__(
        self,
        window: pygame.Surface,
        max_width: int,
        max_height: int,
        ID: int,
        health: int,
        image: pygwidgets.Image,
    ):
        self.health = health

        # выбираем произвольную скорость между -3 и 3, но не ноль
        speed_list = [-3, -2, -1, 1, 2, 3]
        self.speed_x = random.choice(speed_list)

        super().__init__(window, max_width, max_height, ID, image)

    def update(self) -> None:
        if (self.x < 0) or (self.x >= self.max_width):
            self.speed_x = - self.speed_x

        self.x = self.x + self.speed_x
        self.image.setLoc((self.x, self.y))

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
