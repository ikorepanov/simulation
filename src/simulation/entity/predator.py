from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.entity.creature import Creature
from simulation.settings import ATTACK_POWER, PREDATOR_HP, PREDATOR_SPEED

if TYPE_CHECKING:
    from simulation.map import Map

from loguru import logger

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.entity.herbivore import Herbivore
from simulation.pathfinder import Pathfinder
from simulation.settings import PREDATOR


class Predator(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        speed: int = PREDATOR_SPEED,
        hp: int = PREDATOR_HP,
        attack_power: int = ATTACK_POWER,
        prey: type[Entity] = Herbivore,
    ):
        super().__init__(coordinate, speed, hp, prey)

        self.attack_power = attack_power

    def get_sprite(self) -> str:
        return PREDATOR

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
        logger.info(f'Хищник сходил на {self.speed} клетку')

    def finish_resource(self, path: list[Coordinate], map: Map) -> None:
        map.remove_entity(path[0])
        self.occupy_new_position(self.coordinate, path[0], map)

    def bite(self, prey: Herbivore, attack_power: int) -> None:
        prey.loose_hp(attack_power)

    def is_done(self, prey: Herbivore) -> bool:
        return prey.hp <= 0

    def attack(self, path: list[Coordinate], map: Map) -> None:
        herbivore = map.get_entity(path[0])
        if isinstance(herbivore, Herbivore):
            self.bite(herbivore, self.attack_power)
            if self.is_done(herbivore):
                self.finish_resource(path, map)
                # map.remove_entity(path[0])  # NB!!! Надо как-то использовать ранее полученного herbivore для этого...
                # self.occupy_new_position(self.coordinate, path[0], map)
                logger.info('Хищник съел травоядное')
            else:
                logger.info('Хищник укусил травоядное')

    def make_move(self, map: Map) -> None:
        # Ищем путь
        path = Pathfinder().find_path(map, self.coordinate, self.prey)
        if len(path) > 1:  # Далеко
            self.get_closer(path, map)  # Приблизиться
        if len(path) == 1:  # Близко
            self.attack(path, map)  # Атаковать

    #     if path:
    #         if len(path) == 1:
    #             prey_coord = path[0]
    #             self.attack_prey(prey_coord, map)
    #         else:
    #             new_coord = path[self.speed - 1]
    #             self.move_towards(new_coord, map)

    # def move_towards(self, coord: Coordinate, map: Map) -> None:
    #     predator = map.remove_entity(self.coordinate)
    #     map.add_entity(coord, predator)
    #     self.coordinate = coord
    #     logger.info(f'Хищник сходил на {self.speed} клетку')

    # def attack_prey(self, coord: Coordinate, map: Map) -> None:
    #     entity = map.get_entity(coord)
    #     if isinstance(entity, Herbivore):
    #         prey = entity
    #         prey.loose_hp()
    #         logger.info('Хищник укусил травоядное')
    #         if prey.hp == 0:
    #             self.move_towards(coord, map)
    #             logger.info('Хищник съел травоядное')
