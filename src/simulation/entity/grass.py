import pygame
import pygwidgets
from simulation.params import BASE_PATH
from simulation.entity.entity import Entity


class Grass(Entity):
    grass_image = pygame.image.load(BASE_PATH + '/assets/images/grass_small.png')

    def __init__(
        self,
        window: pygame.Surface,
        max_width: int,
        max_height: int,
        ID: int,
        nutrients: int = 10,
    ):
        self.nutrients = nutrients

        image = pygwidgets.Image(window, (0, 0), Grass.grass_image)
        super().__init__(window, max_width, max_height, ID, image)
