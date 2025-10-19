from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.pathfinder import Pathfinder

if TYPE_CHECKING:
    from simulation.map import Map


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
    def make_move(self, map: Map) -> None:
        raise NotImplementedError

    def is_tile_available_for_move(self, coordinate: Coordinate, map: Map) -> bool:
        return map.is_tile_empty(coordinate)

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

    def occupy_new_position(self, old_coord: Coordinate, new_coord: Coordinate, map: Map) -> None:
        entity = map.remove_entity(old_coord)
        map.add_entity(new_coord, entity)
        self.coordinate = new_coord

    def get_exact_same_coordinate(self, coord: Coordinate, map: Map) -> Coordinate:
        for obj in map.entities.keys():
            if obj.x == coord.x and obj.y == coord.y:
                return obj
        return coord  # ?
        # return [obj for obj in map.entities.keys() if obj.x == coord.x and obj.y == coord.y]

    def finish_resource(self, path: list[Coordinate], map: Map) -> None:
        prey_coordinate = self.get_exact_same_coordinate(path[0], map)
        map.remove_entity(path[0])
        self.occupy_new_position(self.coordinate, prey_coordinate, map)
