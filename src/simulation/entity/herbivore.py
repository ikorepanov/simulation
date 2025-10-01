from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.grass import Grass

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.entity.entity import Entity
from simulation.pathfinder import Pathfinder
from simulation.settings import HERBIVORE, HERBIVORE_HP, HERBIVORE_SPEED

from loguru import logger


class Herbivore(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        speed: int = HERBIVORE_SPEED,
        hp: int = HERBIVORE_HP,
        prey: type[Entity] = Grass,
    ):
        super().__init__(coordinate, speed, hp, prey)

    def __repr__(self) -> str:
        return f'Herbivore {id(self)}'

    def get_sprite(self) -> str:
        return HERBIVORE

    def new_coord(self, path: list[Coordinate]) -> Coordinate:
        index_1 = path.index(path[self.speed - 1])
        index_2 = len(path) - 2
        return path[min(index_1, index_2)]

    def occupy_new_position(self, old_coord: Coordinate, new_coord: Coordinate, map: Map) -> None:
        entity = map.remove_entity(old_coord)
        map.add_entity(new_coord, entity)
        self.coordinate = new_coord

    def get_closer(self, path: list[Coordinate], map: Map) -> None:
        new_coord = self.new_coord(path)
        self.occupy_new_position(self.coordinate, new_coord, map)
        logger.info(f'Травоядное сходило на {self.speed} клетку')

    def finish_resource(self, path: list[Coordinate], map: Map) -> None:
        # print(f"""
        # id координаты, на которой стоит трава: {id(path[0])}
        # """)
        map.remove_entity(path[0])
        # print(f"""
        # Айдишники координат до: {[id(key) for key in map.entities.keys()]}
        # """)
        self.occupy_new_position(self.coordinate, path[0], map)
        # print(f"""
        # Айдишники координат после: {[id(key) for key in map.entities.keys()]}
        # """)

    def make_move(self, map: Map) -> None:
        # Ищем путь
        path = Pathfinder().find_path(map, self.coordinate, self.prey)
        if path:
            if len(path) > 1:  # Далеко
                self.get_closer(path, map)  # Приблизиться
            if len(path) == 1:  # Близко
                self.finish_resource(path, map)  # Атаковать
                logger.info('Травоядное съело траву')
        else:
            logger.info('Травоядное курит')

        # path = Pathfinder().find_path(map, self.coordinate, self.prey)
        # if path:
        #     herbivore = map.remove_entity(self.coordinate)
        #     if len(path) == 1:
        #         new_coord = path[0]
        #         logger.info('Травоядное съело траву')
        #     else:
        #         new_coord = path[self.speed - 1]
        #         logger.info(f'Травоядное сходило на {self.speed} клетку')
        #     map.add_entity(new_coord, herbivore)
        #     self.coordinate = new_coord
        # else:
        #     logger.info('Травоядное курит')

    def loose_hp(self, attack_power: int) -> None:
        self.hp -= attack_power
