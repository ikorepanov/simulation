import random
from itertools import count

from loguru import logger

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.grass import Grass
from simulation.game_map import Map
from simulation.settings import (
    HERBIVORE_SPRITE,
    MAX_HERBIVORE_HP,
    MAX_HERBIVORE_SPEED,
    MIN_HERBIVORE_HP,
    MIN_HERBIVORE_SPEED,
)


class Herbivore(Creature):
    _ids = count(1)

    def __init__(
        self,
        speed: int | None = None,
        hp: int | None = None,
        prey_class: type[Grass] = Grass,
    ):
        if speed is None:
            speed = random.randint(MIN_HERBIVORE_SPEED, MAX_HERBIVORE_SPEED)
        if hp is None:
            hp = random.randint(MIN_HERBIVORE_HP, MAX_HERBIVORE_HP)

        super().__init__(speed, hp, prey_class)
        self.id = next(self._ids)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}-{self.id} (HP: {self.hp})'

    def get_sprite(self) -> str:
        return HERBIVORE_SPRITE

    def make_move(self, game_map: Map) -> None:
        path = self.pathfinder.find_path(game_map, self.coord, self.prey_class)
        if path:
            if len(path) > 1:
                self._get_closer(path, game_map)
            if len(path) == 1:
                self._eat_at(path[0], game_map)
        else:
            self._wander_or_idle(game_map)

    def _eat_at(self, coord: Coordinate, game_map: Map) -> None:
        grass = game_map.get_entity_at(coord)
        if grass and isinstance(grass, Grass):
            grass.to_be_eaten()
            self._finish_resource_at(
                coord, game_map
            ) if grass.height <= 0 else logger.info(f'{self} is eating {grass}')

    def _wander_or_idle(self, game_map: Map) -> None:
        what_to_do = ['wander', 'idle']
        weights = (1 / 3, 2 / 3)

        some = random.choices(what_to_do, weights=weights)[0]

        if some == 'wander':
            adjacent_coords = game_map.get_adjacents(self.coord)
            count = len(adjacent_coords)
            new_coord = None
            while count > 0:
                random_coord = random.choice(adjacent_coords)
                if game_map.is_empty_at(random_coord):
                    new_coord = random_coord
                    break
                count -= 1
            if new_coord:
                logger.info(f'{self} is wandering and')
                self._move_to(new_coord, game_map)
            else:
                logger.info(f"{self} want to go somewhere but doesn't have place to go")
        else:
            logger.info(f'{self} chose to stay in place')

    def _loose_hp(self, attack_power: int) -> None:
        self.hp -= attack_power
