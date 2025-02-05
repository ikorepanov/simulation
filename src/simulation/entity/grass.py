import pygame

from simulation.entity.entity import Entity


class Grass(Entity):
    def __init__(
        self,
        ID: int,
        image: pygame.Surface,
        nutrients: int = 10,
    ):
        self.nutrients = nutrients

        super().__init__(ID, image)
