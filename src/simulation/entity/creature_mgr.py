import pygame

from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.grass import Grass
from simulation.params import N_HERBIVORES, N_PREDATORS, N_GRASS


class CreatureMgr:
    def __init__(
        self,
        window: pygame.Surface,
        max_width: int,
        max_height: int,
    ):
        self.window = window
        self.max_width = max_width
        self.max_height = max_height

    def start(self) -> None:
        self.creature_list: list[Herbivore | Predator] = []
        self.entity_list = []

        for num in range(1, N_HERBIVORES + 1):
            herbivore = Herbivore(self.window, self.max_width, self.max_height, num)
            self.creature_list.append(herbivore)

        for num in range(1, N_PREDATORS + 1):
            predator = Predator(self.window, self.max_width, self.max_height, num)
            self.creature_list.append(predator)

        for num in range(1, N_GRASS + 1):
            grass = Grass(self.window, self.max_width, self.max_height, num)
            self.entity_list.append(grass)

    def update(self) -> None:
        for creature in self.creature_list:
            creature.update()

    def draw(self) -> None:
        for entity in self.entity_list:
            entity.draw()

        for creature in self.creature_list:
            creature.draw()
