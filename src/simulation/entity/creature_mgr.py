import pygame
import random
import pygwidgets
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.params import N_HERBIVORES, N_PREDATORS


class CreatureMgr:
    def __init__(self, window, max_width, max_height):
        self.window = window
        self.max_width = max_width
        self.max_height = max_height

    def start(self):
        self.creature_list = []

        for herbivore_num in range(0, N_HERBIVORES):
            herbivore = Herbivore(self.window, self.max_width, self.max_height, 'herbivore_small')
            self.creature_list.append(herbivore)

        for predator_num in range(0, N_PREDATORS):
            predator = Predator(self.window, self.max_width, self.max_height, 'predator_small')
            self.creature_list.append(predator)

    def handle_event(self, event):
        pass

    def update(self):
        for creature in self.creature_list:
            creature.update()

    def draw(self):
        for creature in self.creature_list:
            creature.draw()
