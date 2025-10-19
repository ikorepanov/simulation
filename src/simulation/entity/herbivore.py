from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.grass import Grass

if TYPE_CHECKING:
    from simulation.map import Map

from loguru import logger

from simulation.entity.entity import Entity
from simulation.settings import HERBIVORE, HERBIVORE_HP, HERBIVORE_SPEED


class Herbivore(Creature):
    def __init__(
        self,
        speed: int = HERBIVORE_SPEED,
        hp: int = HERBIVORE_HP,
        prey: type[Entity] = Grass,
    ):
        super().__init__(speed, hp, prey)

    def get_sprite(self) -> str:
        return HERBIVORE

    def get_closer(self, path: list[Coordinate], map: Map) -> None:
        new_coord = self.new_coord(path)
        self.occupy_new_position(self.coordinate, new_coord, map)
        logger.info(f'Травоядное сходило на {self.speed} клетку')

    def wander_or_idle(self) -> None:
        pass

    def make_move(self, map: Map) -> None:
        # path = Pathfinder().find_path(map, self.coordinate, self.prey)  # Ищем путь
        path = self.pathfinder.find_path(map, self.coordinate, self.prey)  # Ищем путь
        if path:
            if len(path) > 1:  # Далеко
                self.get_closer(path, map)  # Приблизиться
            if len(path) == 1:  # Близко
                self.finish_resource(path, map)  # Атаковать
                logger.info('Травоядное съело траву')
        else:
            # self.wander_or_idle()
            logger.info('Травоядное курит')

    def loose_hp(self, attack_power: int) -> None:
        self.hp -= attack_power
