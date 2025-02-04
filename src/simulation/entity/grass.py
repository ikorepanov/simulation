import pygame

from simulation.entity.entity import Entity
from simulation.params import BASE_PATH


class Grass(Entity):
    grass_image = pygame.image.load(BASE_PATH + '/assets/images/grass_small_2.png')

    def __init__(
        self,
        ID: int,
        nutrients: int = 10,
    ):
        self.nutrients = nutrients

        super().__init__(ID, Grass.grass_image)
