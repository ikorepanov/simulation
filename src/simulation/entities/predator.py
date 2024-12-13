import pygame
from pygame import Surface

from simulation.entities.base import Creature


class Predator(Creature):
    def __init__(self, window: Surface, x: int, y: int, speed: int, hp: int, attack_power: int) -> None:
        super().__init__(window, x, y, speed, hp)
        self.image = pygame.image.load('examples/images/predator_small.png')
        self.attack_power = attack_power

    def draw(self) -> None:
        self.window.blit(self.image, (self.x, self.y))

    def make_move(self) -> None:
        pass
