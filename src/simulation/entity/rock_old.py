import pygame

from simulation.entity.entity import Entity


class Rock(Entity):
    def __init__(
        self,
        ID: int,
        image: pygame.Surface,
    ):
        super().__init__(ID, image)
