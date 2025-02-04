import random
from abc import abstractmethod

import pygame
import pygwidgets

from simulation.entity.entity import Entity, OldEntity

from simulation.params import WIDTH


class OldCreature(OldEntity):
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
        if (self.x < 0) or (self.x >= self.max_width - self.width):
            self.speed_x = - self.speed_x

        self.x = self.x + self.speed_x
        self.image.setLoc((self.x, self.y))

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError


class Creature(Entity):
    @abstractmethod
    def __init__(
        self,
        ID: int,
        health: int,
        image: pygame.Surface,
    ):
        self.health = health

        # выбираем произвольную скорость между -3 и 3, но не ноль
        speed_list = [-3, -2, -1, 1, 2, 3]
        self.speed_x = random.choice(speed_list)

        super().__init__(ID, image)

    def update(self) -> None:
        if self.rect is None:
            return

        if (self.rect.left < 0) or (self.rect.right >= WIDTH):
            self.speed_x = - self.speed_x

        self.rect.x = self.rect.x + self.speed_x

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
