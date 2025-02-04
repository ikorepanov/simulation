from pathlib import Path

import pygame

from simulation.entity.creature import Creature


class Herbivore(Creature):
    herbivore_image = pygame.image.load(Path.cwd() / 'src/simulation/assets/images/herbivore_small.png')

    def __init__(
        self,
        ID: int,
        health: int = 7,
    ):
        super().__init__(ID, health, Herbivore.herbivore_image)

    def make_move(self) -> None:
        pass
