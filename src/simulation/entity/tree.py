# import pygame

from simulation.entity.entity import Entity
from simulation.coordinates import Coordinates


class Tree(Entity):
    def __init__(
        self,
        coordinates: Coordinates,
        w: int,
        h: int,
    ):
        super().__init__(coordinates, w, h)
