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
from loguru import logger


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
        # for class_name, number_of_instances in self.entities_to_create.items():
        #     if class_name is Herbivore:
        #         coord = Coordinate(0, 0)
        #         map.add_entity(coord, self.create_entity(class_name, coord))
        #     elif class_name is Grass:
        #         coord = Coordinate(2, 0)
        #         map.add_entity(coord, self.create_entity(class_name, coord))
            # elif class_name is Predator:
            #     coord = Coordinate(0, 2)
            #     map.add_entity(coord, self.create_entity(class_name, coord))
            # elif class_name is Rock:
            #     coord = Coordinate(2, 1)
            #     map.add_entity(coord, self.create_entity(class_name, coord))
        # print('Сущности расставлены!')
        self.execute_callback()
        # logger.info('Сущности расставлены')


class MoveAction(Action):
    def execute(self, map: Map) -> None:
        for entitiy in map.entities.copy().values():
            if isinstance(entitiy, Creature) and entitiy in map.entities.values():
                entitiy.make_move(map)
                self.execute_callback()
