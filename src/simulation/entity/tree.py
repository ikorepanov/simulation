from pathlib import Path

import pygame

from simulation.entity.entity import Entity


class Tree(Entity):
    tree_image = pygame.image.load(Path.cwd() / 'src/simulation/assets/images/tree_small.png')

    def __init__(
        self,
        ID: int,
    ):
        super().__init__(ID, Tree.tree_image)
