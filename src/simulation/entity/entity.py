import random
from abc import ABC, abstractmethod

import pygame
import pygwidgets

from pygame.sprite import Sprite

from simulation.params import WIDTH, USABLE_HEIGHT


class OldEntity(ABC):
    @abstractmethod
    def __init__(
        self,
        window: pygame.Surface,
        max_width: int,
        max_height: int,
        ID: int,
        image: pygwidgets.Image,
    ):
        self.window = window
        self.max_width = max_width
        # self.max_height = max_height
        self.ID = ID
        self.image = image
        rect = self.image.getRect()
        self.width = rect.width
        self.height = rect.height
        # выбираем произвольную начальную позицию
        self.x = random.randrange(0, max_width - self.width, self.width)
        self.y = random.randrange(0, max_height, self.height)
        self.image.setLoc((self.x, self.y))

    def draw(self) -> None:
        self.image.draw()


class Entity(ABC, Sprite):
    @abstractmethod
    def __init__(
        self,
        ID: int,
        image: pygame.Surface,
    ):
        super().__init__()

        self.ID = ID
        self.image = image
        self.rect = self.image.get_rect()
        # выбираем произвольную начальную позицию
        self.rect.x = random.randrange(0, WIDTH - self.rect.width, self.rect.width)
        self.rect.y = random.randrange(0, USABLE_HEIGHT, self.rect.height)
