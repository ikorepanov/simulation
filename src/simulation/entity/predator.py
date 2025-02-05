import pygame

from simulation.entity.creature import Creature


class Predator(Creature):
    def __init__(
        self,
        ID: int,
        image: pygame.Surface,
        health: int = 8,
        attack_power: int = 10,
    ):
        self.attack_power = attack_power

        super().__init__(ID, image, health)

    def make_move(self) -> None:
        pass
