import pygame as pg
from pygame.sprite import Sprite

from simulation.params import GREEN


class Rock(Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
    ):
        super().__init__()

        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
