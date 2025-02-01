import random
from abc import ABC, abstractmethod

import pygame
import pygwidgets


class Entity(ABC):
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
        self.x = random.randrange(0, max_width, self.width)
        self.y = random.randrange(0, max_height, self.height)
        self.image.setLoc((self.x, self.y))

    def draw(self) -> None:
        self.image.draw()
