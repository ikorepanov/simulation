from __future__ import annotations

from abc import abstractmethod
from typing import Any, TYPE_CHECKING

from pygame.sprite import AbstractGroup

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.coordinate import Coordinate


class Creature(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int],
        velocity: int,
        hp: int,
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        sprite_groups = (map.game.creatures,) + (class_specific_groups or ())
        super().__init__(map, color, sprite_groups)

        self.map = map
        self.velocity = velocity
        self.hp = hp

        self.show_coordinate()

        self.speed_x = 0

    def get_target_entity_positions(self, class_name: Entity) -> list[Coordinate]:
        # Получить инфу о координатах всех имеющихся травоядных / травы
        return [key for key, val in self.map.entities.items() if val == class_name]

    def choose_preferable_target(self, options: list[Coordinate]) -> Coordinate:
        # Выбираем ближайшую цель
        # Здесь будет реализован алгоритм поиска пути
        pass

    def check_if_movement_is_possible(self) -> bool:
        # Проверить - возможно ли "шагнуть" на ту или иную клетку
        pass

    @abstractmethod
    def make_move(self, target_coordinate: Coordinate) -> None:
        # "Сделать шаг" по направлению к цели
        raise NotImplementedError

    def check_if_collide(self) -> bool:
        # Проверяем, приблизились ли вплотную к цели
        pass

    def act_as_intendent(self) -> None:
        # Атаковать - для хищников, есть (траву) - для травоядных
        pass

    def show_coordinate(self) -> None:
        print(f'X is {self.coordinate.x}')
        print(f'Y is {self.coordinate.y}')
