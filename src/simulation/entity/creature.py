from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.pathfinder import Pathfinder

if TYPE_CHECKING:
    from simulation.game_map import Map


class Creature(Entity):
    pathfinder = Pathfinder()

    def __init__(
        self,
        speed: int,
        hp: int,
        prey: type[Entity],
        coordinate: Coordinate = Coordinate(0, 0),
    ):
        self.speed = speed
        self.hp = hp
        self.prey = prey
        self.coordinate = coordinate

    @abstractmethod
    def make_move(self, game_map: Map) -> None:
        raise NotImplementedError

    def is_tile_available_for_move(self, coordinate: Coordinate, game_map: Map) -> bool:
        return game_map.is_empty_at(coordinate)

    def check_if_movement_is_possible(self) -> bool:
        # Проверить - возможно ли "шагнуть" на ту или иную клетку
        is_possible: bool
        return is_possible

    def check_if_collide(self) -> bool:
        # Проверяем, приблизились ли вплотную к цели
        is_collide: bool
        return is_collide

    def act_as_intendent(self) -> None:
        # Атаковать - для хищников, есть (траву) - для травоядных
        pass

    def new_coord(self, path: list[Coordinate]) -> Coordinate:
        index_1 = path.index(path[self.speed - 1])
        index_2 = len(path) - 2
        return path[min(index_1, index_2)]

    def occupy_new_position(self, old_coord: Coordinate, new_coord: Coordinate, game_map: Map) -> None:
        entity = game_map.remove_entity_at(old_coord)
        game_map.add_entity_at(new_coord, entity)
        self.coordinate = new_coord

    def get_exact_same_coordinate(self, coord: Coordinate, game_map: Map) -> Coordinate:  # Надо этот метод убирать (раз уж hash и eq у нас переопределены...)
        for obj in game_map.entities.keys():
            if obj.x == coord.x and obj.y == coord.y:
                return obj
        return coord  # ?
        # return [obj for obj in game_map.entities.keys() if obj.x == coord.x and obj.y == coord.y]

    def finish_resource(self, path: list[Coordinate], game_map: Map) -> None:
        prey_coordinate = self.get_exact_same_coordinate(path[0], game_map)
        game_map.remove_entity_at(path[0])
        self.occupy_new_position(self.coordinate, prey_coordinate, game_map)
