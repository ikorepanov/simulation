from pathlib import Path

import pygame

from simulation.entity.entity import Entity


class Rock(Entity):
    rock_image = pygame.image.load(Path.cwd() / 'src/simulation/assets/images/rock_small.png')

    def __init__(
        self,
        ID: int,
    ):
        super().__init__(ID, Rock.rock_image)
