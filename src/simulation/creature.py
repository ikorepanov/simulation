from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.coordinate_shift import CoordinateShift
from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map


class Creature(Entity):
    def __init__(
        self,
        coordinate: Coordinate,
        speed: int,  # сколько клеток может пройти за 1 ход
        hp: int,  # Health Points ("здоровье")
    ):
        # "... координата нужна только тому существу, которое ходит.
        # Поэтому entities должны хранить координату только начиная с уровня Creature."
        self.coordinate = coordinate
        self.speed = speed
        self.hp = hp

        # self.state = 'idle'
        # self.wait_time = 0
        # self.prey: type[Entity] = Entity
        # self.path: list[Coordinate] = []
        # self.next_node: Coordinate | None = None

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
        return not map.is_tile_occupied(coordinate)

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

    def update(self) -> None:
        pass
        # if self.state == 'sniffing':
        #     self.pick_up_the_scent()
        #     if self.path:
        #         print(f'Path to prey: {[(node.x, node.y) for node in self.path]}')
        #         self.state = 'checking'  # 'waiting'

        # if self.state == 'checking':
        #     if self.path:
        #         self.next_node = self.path.pop(0)
        #         self.state = 'moving'
        #     else:
        #         print('STOP')
        #         self.state = 'stop'

        # if self.state == 'moving':
        #     print(self.next_node.x, self.next_node.y)
        #     print([(node.x, node.y) for node in self.path])
        #     if self.next_node:
        #         if self.rect.x != self.next_node.x * TILESIZE:
        #             self.rect.x += self.speed
        #             if self.rect.x >= self.next_node.x * TILESIZE:
        #                 # self.state = 'stop'
        #                 # self.state = 'waiting'
        #                 self.state = 'checking'
        #                 self.wait_time = pygame.time.get_ticks()
        #         if self.rect.y != self.next_node.y * TILESIZE:
        #             self.rect.y += self.speed
        #             if self.rect.y >= self.next_node.y * TILESIZE:
        #                 # self.state = 'stop'
        #                 # self.state = 'waiting'
        #                 self.state = 'checking'
        #                 self.wait_time = pygame.time.get_ticks()

        # if self.state == 'stop':
        #     pass

        # if self.state == 'waiting':
        #     now = pygame.time.get_ticks()
        #     if now - self.wait_time >= 2000:
        #         if self.path:
        #             self.next_node = self.path.pop(0)
        #             self.state = 'moving'
        #         else:
        #             print('STOP')
        #             self.state = 'stop'
