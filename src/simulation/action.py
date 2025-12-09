import random
from abc import ABC, abstractmethod

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.entity import Entity
from simulation.exceptions import NoUnoccupiedCoordsError
from simulation.game_map import Map
from simulation.settings import NUMBER_OF_ATTEMPTS


class Action(ABC):
    @abstractmethod
    def execute(self, game_map: Map) -> None:
        raise NotImplementedError


class PlaceEntitiesAction(Action):
    def __init__(self, entities_to_place: list[Entity]) -> None:
        self.entities_to_place = entities_to_place

    def _get_unoccupied_coord(self, game_map: Map) -> Coordinate:
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coord = Coordinate(
                x=random.randrange(game_map.width), y=random.randrange(game_map.height)
            )
            if not game_map.is_empty_at(coord):
                attempts += 1
                continue
            return coord
        raise NoUnoccupiedCoordsError()

    def execute(self, game_map: Map) -> None:
        for entity in self.entities_to_place:
            coord = self._get_unoccupied_coord(game_map)
            if isinstance(entity, Creature):
                entity.coord = coord
            game_map.add_entity_at(coord, entity)


class MoveAction(Action):
    def _get_creatures(self, game_map: Map) -> list[Creature]:
        return [
            entity
            for entity in game_map.entities.values()
            if isinstance(entity, Creature)
        ]

    def _is_creature_still_alive(self, creature: Creature, game_map: Map) -> bool:
        return creature in game_map.entities.values()

    def execute(self, game_map: Map) -> None:
        creatures = self._get_creatures(game_map)
        for creature in creatures:
            if self._is_creature_still_alive(creature, game_map):  # Может уже не быть
                creature.make_move(game_map)  # в оригинале, но всё ещё быть в копии
