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

    def make_move(self, map: Map) -> None:
        path = Pathfinder().find_path(map, self.coordinate, self.prey)
        if path:
            if len(path) == 1:
                prey_coord = path[0]
                self.attack_prey(prey_coord, map)
            else:
                new_coord = path[self.speed - 1]
                self.move_towards(new_coord, map)

    def move_towards(self, coord: Coordinate, map: Map) -> None:
        predator = map.remove_entity(self.coordinate)
        map.add_entity(coord, predator)
        self.coordinate = coord
        # logger.info(f'Хищник сходил на {self.speed} клетку')

    def attack_prey(self, coord: Coordinate, map: Map) -> None:
        entity = map.get_entity(coord)
        if isinstance(entity, Herbivore):
            prey = entity
            prey.loose_hp()
            # print('Хищник укусил травоядное')
            if prey.hp == 0:
                self.move_towards(coord, map)
                # print('Хищник съел травоядное')
