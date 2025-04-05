from abc import ABC

import pygame as pg
from pygame.sprite import Sprite

from simulation.settings import GREEN


class Entity(ABC, Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
    ):
        super().__init__()

        self.image = pg.Surface((w, h))  # Every sprite has to have (1)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()  # Every sprite has to have (2)
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        pass
