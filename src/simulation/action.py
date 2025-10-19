import random
from abc import ABC, abstractmethod
from typing import Callable

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.entity import Entity
from simulation.exceptions import NoUnoccupiedTilesError
from simulation.map import Map
from simulation.settings import NUMBER_OF_ATTEMPTS


class Action(ABC):
    @abstractmethod
    def execute(self, map: Map) -> None:
        raise NotImplementedError

    def register_callback(self, fn: Callable[..., None]) -> None:
        self.cb = fn

    def execute_callback(self) -> None:
        self.cb()


class PlaceEntitiesAction(Action):
    def __init__(self, entities_to_place: list[Entity]) -> None:
        self.entities_to_place = entities_to_place

    def _get_unoccupied_coordinate(self, map: Map) -> Coordinate:
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

    def execute(self, map: Map) -> None:
        for entity in self.entities_to_place:
            coord = self._get_unoccupied_coordinate(map)
            if isinstance(entity, Creature):
                entity.coordinate = coord
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
