from simulation.entity.entity import Entity
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.rock import Rock
from simulation.entity.predator import Predator
from simulation.entity.tree import Tree

from simulation.settings import GRASS_NUMBER, HERBIVORE_NUMBER, PREDATOR_NUMBER, ROCK_NUMBER, TREE_NUMBER


class EntityCreator:
    def __init__(self) -> None:
        self.entity_instance_counts: dict[type[Entity], int] = {
            Predator: PREDATOR_NUMBER,
            Herbivore: HERBIVORE_NUMBER,
            Rock: ROCK_NUMBER,
            Tree: TREE_NUMBER,
            Grass: GRASS_NUMBER,
        }

    def run(self) -> list[Entity]:
        return [cls() for cls, count in self.entity_instance_counts.items() for _ in range(count)]
