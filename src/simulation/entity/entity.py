# import random
from abc import ABC
from pathlib import Path

import pygame as pg
from pygame.sprite import Sprite

# from simulation.params import USABLE_HEIGHT, WIDTH

from simulation.coordinates import Coordinates
from simulation.params import GREEN


class Entity(ABC, Sprite):
    def __init__(
        self,
        # id: int,
        coordinates: Coordinates,
        # image: pygame.Surface,
        w: int,
        h: int,
    ):
        super().__init__()

        # self.id = id
        # self.image = image
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.coordinates = coordinates
        self.rect.x = self.coordinates.x
        self.rect.y = self.coordinates.y
        # выбираем произвольную начальную позицию
        # self.rect.x = random.randrange(0, WIDTH - self.rect.width, self.rect.width)
        # self.rect.y = random.randrange(0, USABLE_HEIGHT, self.rect.height)

    @staticmethod
    def load_image(file_name: str) -> pg.Surface:
        return pg.image.load(Path.cwd() / f'src/simulation/assets/images/{file_name}.png').convert()
