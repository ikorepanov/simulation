from simulation.params import BASE_PATH
import pygame

from simulation.entity.entity import Entity


class Rock(Entity):
    rock_image = pygame.image.load(BASE_PATH + '/assets/images/rock_small.png')

    def __init__(
        self,
        ID: int,
    ):
        super().__init__(ID, Rock.rock_image)
