import pygame

from simulation.entity.creature import Creature


class Herbivore(Creature):
    def __init__(
        self,
        ID: int,
        image: pygame.Surface,
        health: int = 7,
    ):
        super().__init__(ID, image, health)

    def make_move(self) -> None:
        pass
