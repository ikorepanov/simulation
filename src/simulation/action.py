import random
from abc import ABC, abstractmethod
from typing import Callable

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.entity import Entity
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.rock import Rock
from simulation.entity.tree import Tree
from simulation.exceptions import NoUnoccupiedTilesError
from simulation.map import Map
from simulation.settings import (
    GRASS_NUMBER,
    HERBIVORE_NUMBER,
    NUMBER_OF_ATTEMPTS,
    PREDATOR_NUMBER,
    ROCK_NUMBER,
    TREE_NUMBER,
)


class Action(ABC):
    @abstractmethod
    def execute(self, map: Map) -> None:
        raise NotImplementedError

    def register_callback(self, fn: Callable[..., None]) -> None:
        self.cb = fn

    def execute_callback(self) -> None:
        self.cb()


class PlaceEntitiesAction(Action):
    def __init__(self) -> None:
        self.entities_to_create: dict[type[Entity], int] = {
            Predator: PREDATOR_NUMBER,
            Herbivore: HERBIVORE_NUMBER,
            Rock: ROCK_NUMBER,
            Tree: TREE_NUMBER,
            Grass: GRASS_NUMBER,
        }

    def generate_initial_coordinate(self, map: Map) -> Coordinate:
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coordinate = Coordinate(
                x=random.randrange(map.width),
                y=random.randrange(map.height)
            )
            if not map.is_tile_empty(coordinate):
                attempts += 1
                continue
            return coordinate
        raise NoUnoccupiedTilesError()

    def create_entity(self, entity_class: type[Entity], coord: Coordinate) -> Entity:
        if entity_class is Predator:
            return Predator(coord)
        elif entity_class is Herbivore:
            return Herbivore(coord)
        elif entity_class is Rock:
            return Rock()
        elif entity_class is Tree:
            return Tree()
        elif entity_class is Grass:
            return Grass()
        else:
            raise ValueError(entity_class)

    def execute(self, map: Map) -> None:
        for class_name, number_of_instances in self.entities_to_create.items():
            for _ in range(number_of_instances):
                coord = self.generate_initial_coordinate(map)
                entity = self.create_entity(class_name, coord)
                map.add_entity(coord, entity)
        self.execute_callback()


class MoveAction(Action):
    def _get_creatures(self, map: Map) -> list[Creature]:
        return [entity for entity in map.entities.values() if isinstance(entity, Creature)]

    def _is_creature_still_alive(self, creature: Creature, map: Map) -> bool:
        return creature in map.entities.values()

    def execute(self, map: Map) -> None:
        creatures = self._get_creatures(map)
        for creature in creatures:
            if self._is_creature_still_alive(creature, map):
                creature.make_move(map)
                self.execute_callback()
