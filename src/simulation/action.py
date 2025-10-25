import random
from abc import ABC, abstractmethod
from typing import Callable

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.entity import Entity
from simulation.exceptions import NoUnoccupiedTilesError
from simulation.game_map import Map
from simulation.settings import NUMBER_OF_ATTEMPTS


class Action(ABC):
    @abstractmethod
    def execute(self, game_map: Map) -> None:
        raise NotImplementedError

    def register_callback(self, fn: Callable[..., None]) -> None:
        self.cb = fn

    def execute_callback(self) -> None:
        self.cb()


class PlaceEntitiesAction(Action):
    def __init__(self, entities_to_place: list[Entity]) -> None:
        self.entities_to_place = entities_to_place

    def _get_unoccupied_coordinate(self, game_map: Map) -> Coordinate:
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coordinate = Coordinate(
                x=random.randrange(game_map.width),
                y=random.randrange(game_map.height)
            )
            if not game_map.is_empty_at(coordinate):
                attempts += 1
                continue
            return coordinate
        raise NoUnoccupiedTilesError()

    def execute(self, game_map: Map) -> None:
        for entity in self.entities_to_place:
            coord = self._get_unoccupied_coordinate(game_map)
            if isinstance(entity, Creature):
                entity.coordinate = coord
            game_map.add_entity_at(coord, entity)
        self.execute_callback()


class MoveAction(Action):
    def _get_creatures(self, game_map: Map) -> list[Creature]:
        return [entity for entity in game_map.entities.values() if isinstance(entity, Creature)]

    def _is_creature_still_alive(self, creature: Creature, game_map: Map) -> bool:
        return creature in game_map.entities.values()

    def execute(self, game_map: Map) -> None:
        creatures = self._get_creatures(game_map)
        for creature in creatures:
            if self._is_creature_still_alive(creature, game_map):
                creature.make_move(game_map)
                self.execute_callback()
