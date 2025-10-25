from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.grass import Grass

if TYPE_CHECKING:
    from simulation.game_map import Map

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

    def get_closer(self, path: list[Coordinate], game_map: Map) -> None:
        new_coord = self.new_coord(path)
        self.occupy_new_position(self.coord, new_coord, game_map)
        logger.info(f'Травоядное сходило на {self.speed} клетку')

    def wander_or_idle(self) -> None:
        pass

    def make_move(self, game_map: Map) -> None:
        # path = Pathfinder().find_path(game_map, self.coord, self.prey)  # Ищем путь
        path = self.pathfinder.find_path(game_map, self.coord, self.prey)  # Ищем путь
        if path:
            if len(path) > 1:  # Далеко
                self.get_closer(path, game_map)  # Приблизиться
            if len(path) == 1:  # Близко
                self.finish_resource(path, game_map)  # Атаковать
                logger.info('Травоядное съело траву')
        else:
            # self.wander_or_idle()
            logger.info('Травоядное курит')

    def loose_hp(self, attack_power: int) -> None:
        self.hp -= attack_power
