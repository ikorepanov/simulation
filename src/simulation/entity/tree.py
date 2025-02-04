from simulation.params import BASE_PATH
import pygame

from simulation.entity.entity import Entity


class Tree(Entity):
    tree_image = pygame.image.load(BASE_PATH + '/assets/images/tree_small.png')

    def __init__(
        self,
        ID: int,
    ):
        super().__init__(ID, Tree.tree_image)
