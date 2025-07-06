from abc import ABC

import pygame
from pygame.sprite import Sprite

from simulation.settings import TILESIZE


class Entity(Sprite, ABC):
    def __init__(
        self,
        color: tuple[int, int, int],
    ):
        super().__init__()

        self.image = pygame.Surface((TILESIZE, TILESIZE))  # Every sprite has to have (1)
        self.image.fill(color)
        self.rect = self.image.get_rect()  # Every sprite has to have (2)

    def __new__(cls, *args, **kwargs):  # type: ignore
        if cls is Entity:
            raise TypeError("Can't instantiate abstract class Entity (even without any abstract method)")
        return super().__new__(cls)

    def place_rect_on_corresponding_coordinate(self, x: int, y: int) -> None:
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
