from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.coordinate_shift import CoordinateShift
from simulation.entity.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map


class Creature(Entity):
    def __init__(
        self,
        speed: int,  # сколько клеток может пройти за 1 ход
        hp: int,  # Health Points ("здоровье")
        prey: type[Entity],
        coordinate: Coordinate = Coordinate(0, 0),
    ):
        # "... координата нужна только тому существу, которое ходит.
        # Поэтому entities должны хранить координату только начиная с уровня Creature."
        self.coordinate = coordinate
        self.speed = speed
        self.hp = hp
        self.prey = prey

    @abstractmethod
    def make_move(self, map: Map) -> None:
        raise NotImplementedError

    # Метод, который возвращает все координаты - доступных для перемещения полей
    def get_available_move_tiles(self, map: Map) -> set[Coordinate]:
        result: set[Coordinate] = set()

        for shift in self.get_creature_moves():
            if self.coordinate.can_shift(shift):
                new_coordinate = self.coordinate.shift(shift)
                if self.is_tile_available_for_move(new_coordinate, map):
                    result.add(new_coordinate)
        return result

    # Получить сдвиги для сущности
    def get_creature_moves(self) -> set[CoordinateShift]:
        result: set[CoordinateShift] = set()

        # x = self.coordinate.x
        # y = self.coordinate.y

        # for pair in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        for pair in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            result.add(CoordinateShift(pair[0], pair[1]))
        return result

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
