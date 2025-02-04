import pygame

from simulation.entity.creature import Creature
from simulation.params import BASE_PATH


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
