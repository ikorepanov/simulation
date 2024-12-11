from simulation.entities.base import Creature
import pygame


class Predator(Creature):
    def __init__(self, window, x, y, speed, hp, attack_power):
        super().__init__(window, x, y, speed, hp)
        self.image = pygame.image.load('examples/images/predator_small.png')
        self.attack_power = attack_power

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def make_move(self):
        pass
