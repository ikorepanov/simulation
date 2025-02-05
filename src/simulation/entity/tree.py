import pygame

from simulation.entity.entity import Entity


class Tree(Entity):
    def __init__(
        self,
        ID: int,
        image: pygame.Surface,
    ):
        super().__init__(ID, image)
