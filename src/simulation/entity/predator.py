from pathlib import Path

import pygame

from simulation.entity.creature import Creature


class Predator(Creature):
    predator_image = pygame.image.load(Path.cwd() / 'src/simulation/assets/images/predator_small.png')

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
