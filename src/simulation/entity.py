from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

import pygame as pg
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.settings import TILESIZE


class Entity(ABC, Sprite):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int],
        w: int = TILESIZE,
        h: int = TILESIZE,
    ):
        super().__init__()

        self.map = map
        self.image = pg.Surface((w, h))  # Every sprite has to have (1)
        self.image.fill(color)
        self.rect = self.image.get_rect()  # Every sprite has to have (2)
        coordinate = self.map.set_coordinate()
        self.rect.x = coordinate.abscissa.value
        self.rect.y = coordinate.ordinate.value

    def update(self) -> None:
        pass
