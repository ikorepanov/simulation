import random
from abc import ABC, abstractmethod

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


class PlaceEntitiesAction(Action):
    def __init__(self, entities_to_place: list[Entity]) -> None:
        self.entities_to_place = entities_to_place

    def _get_unoccupied_coord(self, game_map: Map) -> Coordinate:
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coord = Coordinate(
                x=random.randrange(game_map.width),
                y=random.randrange(game_map.height)
            )
            if not game_map.is_empty_at(coord):
                attempts += 1
                continue
            return coord
        raise NoUnoccupiedTilesError()

    def execute(self, game_map: Map) -> None:
        for entity in self.entities_to_place:
            coord = self._get_unoccupied_coord(game_map)
            if isinstance(entity, Creature):
                entity.coord = coord
            game_map.add_entity_at(coord, entity)

        # ent_1 = self.entities_to_place[0]
        # # coord = Coordinate(2, 2)  # Расстановка №1 для отдатки move in circles
        # coord = Coordinate(3, 2)  # Расстановка №2 для отдатки move in circles
        # ent_1.coord = coord
        # game_map.add_entity_at(coord, ent_1)

        # ent_2 = self.entities_to_place[1]
        # # coord = Coordinate(0, 0)  # Расстановка №1 для отдатки move in circles
        # coord = Coordinate(0, 0)  # Расстановка №2 для отдатки move in circles
        # ent_2.coord = coord
        # game_map.add_entity_at(coord, ent_2)

        # ent_3 = self.entities_to_place[2]
        # # coord = Coordinate(1, 2)  # Расстановка №1 для отдатки move in circles
        # coord = Coordinate(3, 0)  # Расстановка №2 для отдатки move in circles
        # ent_3.coord = coord
        # game_map.add_entity_at(coord, ent_3)


class MoveAction(Action):
    def _get_creatures(self, game_map: Map) -> list[Creature]:
        return [entity for entity in game_map.entities.values() if isinstance(entity, Creature)]

    def _is_creature_still_alive(self, creature: Creature, game_map: Map) -> bool:
        return creature in game_map.entities.values()

    def execute(self, game_map: Map) -> None:
        creatures = self._get_creatures(game_map)
        for creature in creatures:
            if self._is_creature_still_alive(creature, game_map):  # Может уже не быть в оригинале, но всё ещё быть в копии
                creature.make_move(game_map)
