import pygame
import pygwidgets

from simulation.entity.creature import Creature, OldCreature
from simulation.params import BASE_PATH


class OldHerbivore(OldCreature):
    herbivore_image = pygame.image.load(BASE_PATH + '/assets/images/herbivore_small.png')

    def __init__(
        self,
        window: pygame.Surface,
        max_width: int,
        max_height: int,
        ID: int,
        health: int = 7,
    ):
        image = pygwidgets.Image(window, (0, 0), Herbivore.herbivore_image)
        super().__init__(window, max_width, max_height, ID, health, image)

    def make_move(self) -> None:
        pass


class Herbivore(Creature):
    herbivore_image = pygame.image.load(BASE_PATH + '/assets/images/herbivore_small.png')

    def __init__(
        self,
        ID: int,
        health: int = 7,
    ):
        super().__init__(ID, health, Herbivore.herbivore_image)

    def make_move(self) -> None:
        pass
