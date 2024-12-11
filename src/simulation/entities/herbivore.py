from simulation.entities.base import Creature
import pygame


class Herbivore(Creature):
    def __init__(self, window, x, y, speed, hp):
        super().__init__(window, x, y, speed, hp)
        self.image = pygame.image.load('examples/images/herbivore_small.png')

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def make_move(self):
        pass
