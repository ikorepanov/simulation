from abc import ABC

import pygame as pg
from pygame.sprite import Sprite

from simulation.coordinate import Coordinate


class Entity(ABC, Sprite):
    def __init__(
        self,
        coordinate: Coordinate,
        w: int,
        h: int,
        color: tuple[int, int, int],
    ):
        super().__init__()

        self.image = pg.Surface((w, h))  # Every sprite has to have (1)
        self.image.fill(color)
        self.rect = self.image.get_rect()  # Every sprite has to have (2)
        self.rect.x = coordinate.abscissa.value
        self.rect.y = coordinate.ordinate.value

    def update(self) -> None:
        pass
