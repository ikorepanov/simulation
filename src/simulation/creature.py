from __future__ import annotations

from typing import Any, TYPE_CHECKING

from pygame.sprite import AbstractGroup

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

import pygame

from simulation.coordinate import Coordinate
from simulation.settings import WIDTH


class Creature(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int],
        speed: int,
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        sprite_groups = (map.game.creatures,) + (class_specific_groups or ())
        super().__init__(map, color, sprite_groups)

        self.speed = speed
        self.state = 'moving'
        self.wait_time = 0

    def choose_preferable_target(self, options: list[Coordinate]) -> Coordinate:
        # Выбираем ближайшую цель
        # Здесь будет реализован алгоритм поиска пути
        coordinate: Coordinate
        return coordinate

    def check_if_movement_is_possible(self) -> bool:
        # Проверить - возможно ли "шагнуть" на ту или иную клетку
        is_possible: bool
        return is_possible

    def make_move(self, target_coordinate: Coordinate) -> None:
        # "Сделать шаг" по направлению к цели
        pass

    def check_if_collide(self) -> bool:
        # Проверяем, приблизились ли вплотную к цели
        is_collide: bool
        return is_collide

    def act_as_intendent(self) -> None:
        # Атаковать - для хищников, есть (траву) - для травоядных
        pass

    def update(self) -> None:
        if self.state == 'moving':
            self.rect.x += self.speed
            if self.rect.right >= WIDTH:
                self.rect.left = 0
                self.state = 'waiting'
                self.wait_time = pygame.time.get_ticks()

        elif self.state == 'waiting':
            now = pygame.time.get_ticks()
            if now - self.wait_time >= 2000:
                self.state = 'moving'
