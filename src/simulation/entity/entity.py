import random
from abc import ABC, abstractmethod

import pygame
from pygame.sprite import Sprite

from simulation.params import USABLE_HEIGHT, WIDTH


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
