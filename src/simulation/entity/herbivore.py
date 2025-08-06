from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.exceptions import CantFindPathError
from simulation.entity.grass import Grass

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.pathfinder import Pathfinder
from simulation.settings import HERBIVORE, HERBIVORE_HP, HERBIVORE_SPEED


class Herbivore(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        speed: int = HERBIVORE_SPEED,
        hp: int = HERBIVORE_HP,
    ):
        super().__init__(coordinate, speed, hp)

        self.prey = Grass
        self.state = 'waiting'

    def get_sprite(self) -> str:
        return HERBIVORE

    def make_move(self, map: Map) -> None:
        # print('Herbivore has just made move!')

        # if self.state == 'moving':
        #     self.move_towards()
        # if self.state == 'eating':
        #     self.eat_grass()
        try:
            path = Pathfinder().find_path(map, self.coordinate, self.prey)
        except CantFindPathError as error:
            print(f"Can't Find Path Error: {error}")
            sys.exit(1)
        print(f'NB! Путь найден: {[(node.x, node.y) for node in path]}')

    def move_towards(self) -> None:
        pass

    def eat_grass(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
