from abc import ABC

import pygame as pg
from pygame.sprite import Sprite


from simulation.settings import TILESIZE


class Entity(ABC, Sprite):
    def __init__(
        self,
        map,
        # coordinate: Coordinate,
        color: tuple[int, int, int],
        w: int = TILESIZE,
        h: int = TILESIZE,
    ):
        super().__init__()

        self.map = map
        self.image = pg.Surface((w, h))  # Every sprite has to have (1)
        self.image.fill(color)
        self.rect = self.image.get_rect()  # Every sprite has to have (2)
        coordinate = map.set_coordinate()
        self.rect.x = coordinate.abscissa.value
        self.rect.y = coordinate.ordinate.value

    def update(self) -> None:
        pass
