import pygame
from pygame import Surface

from simulation.entities.base import Creature


class Herbivore(Creature):
    def __init__(self, window: Surface, x: int, y: int, speed: int, hp: int) -> None:
        super().__init__(window, x, y, speed, hp)
        self.image = pygame.image.load('examples/images/herbivore_small.png')

    def draw(self) -> None:
        self.window.blit(self.image, (self.x, self.y))

    def make_move(self) -> None:
        pass
