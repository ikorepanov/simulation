import pygame
import pygwidgets

from simulation.entity.creature import Creature, OldCreature
from simulation.params import BASE_PATH


class OldPredator(OldCreature):
    predator_image = pygame.image.load(BASE_PATH + '/assets/images/predator_small.png')

    def __init__(
        self,
        window: pygame.Surface,
        max_width: int,
        max_height: int,
        ID: int,
        health: int = 8,
        attack_power: int = 10,
    ):
        self.attack_power = attack_power

        image = pygwidgets.Image(window, (0, 0), OldPredator.predator_image)
        super().__init__(window, max_width, max_height, ID, health, image)

    def make_move(self) -> None:
        pass


class Predator(Creature):
    predator_image = pygame.image.load(BASE_PATH + '/assets/images/predator_small.png')

    def __init__(
        self,
        ID: int,
        health: int = 8,
        attack_power: int = 10,
    ):
        self.attack_power = attack_power

        super().__init__(ID, health, Predator.predator_image)

    def make_move(self) -> None:
        pass
