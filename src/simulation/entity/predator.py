import random
from itertools import count

from loguru import logger

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.herbivore import Herbivore
from simulation.game_map import Map
from simulation.pathfinder import Pathfinder
from simulation.settings import (
    MAX_ATTACK_POWER,
    MIN_ATTACK_POWER,
    PREDATOR_HP,
    PREDATOR_SPEED,
    PREDATOR_SPRITE,
)


class Predator(Creature):
    _ids = count(1)

    def __init__(
        self,
        speed: int = PREDATOR_SPEED,
        hp: int = PREDATOR_HP,
        prey_class: type[Herbivore] = Herbivore,
        attack_power: int = random.randint(MIN_ATTACK_POWER, MAX_ATTACK_POWER),
    ):
        super().__init__(speed, hp, prey_class)

        self.attack_power = attack_power
        self.prev_coords: list[Coordinate] = []
        self.id = next(self._ids)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}-{self.id} (a.p.: {self.attack_power})'

    def get_sprite(self) -> str:
        return PREDATOR_SPRITE

    def make_move(self, game_map: Map) -> None:
        if self._is_in_circles():
            logger.info(f'{self} remains in place to avoid walking in circles')
            self.prev_coords.clear()
        else:
            path = Pathfinder().find_path(game_map, self.coord, self.prey_class)
            if len(path) > 1:
                self.prev_coords.append(self.coord)
                if len(self.prev_coords) > 4:
                    self.prev_coords.pop(0)
                self._get_closer(path, game_map)
            if len(path) == 1:
                self._attack_at(path[0], game_map)

    def _is_in_circles(self) -> bool:
        if len(self.prev_coords) > 3:
            return (
                self.prev_coords[0] == self.prev_coords[2]
                and self.prev_coords[1] == self.prev_coords[3]
            )
        else:
            return False

    def _attack_at(self, coord: Coordinate, game_map: Map) -> None:
        herbivore = game_map.get_entity_at(coord)
        if herbivore and isinstance(herbivore, Herbivore):
            herbivore._loose_hp(self.attack_power)
            self._finish_resource_at(
                coord, game_map
            ) if herbivore.hp <= 0 else logger.info(f'{self} bit {herbivore}')
