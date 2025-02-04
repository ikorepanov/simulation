from pathlib import Path

import pygame

from simulation.entity.entity import Entity


class Grass(Entity):
    grass_image = pygame.image.load(Path.cwd() / 'src/simulation/assets/images/grass_small_2.png')

    def __init__(
        self,
        ID: int,
        nutrients: int = 10,
    ):
        self.nutrients = nutrients

        super().__init__(ID, Grass.grass_image)
