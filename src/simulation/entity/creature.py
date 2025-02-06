import random
from abc import abstractmethod

import pygame

from simulation.entity.entity import Entity
from simulation.params import WIDTH


class Creature(Entity):
    def __init__(
        self,
        ID: int,
        image: pygame.Surface,
        health: int,
    ):
        self.health = health

        # выбираем произвольную скорость между -3 и 3, но не ноль
        speed_list = [-3, -2, -1, 1, 2, 3]
        self.x_speed = random.choice(speed_list)

        super().__init__(ID, image)

    def update(self) -> None:
        if self.rect is None:
            return

        if (self.rect.left < 0) or (self.rect.right >= WIDTH):
            self.x_speed = - self.x_speed

        self.rect.x += self.x_speed

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
