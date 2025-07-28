from __future__ import annotations

from simulation.coordinate import Coordinate
from simulation.creature import Creature
from simulation.grass import Grass
from simulation.settings import HERBIVORE_HP, HERBIVORE_SPEED, VORTEX
# from simulation.map import Map
from simulation.pathfinder import Pathfinder, CantFindPathError
import sys


class Herbivore(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        color: tuple[int, int, int] = VORTEX,
        speed: int = HERBIVORE_SPEED,
        hp: int = HERBIVORE_HP,
    ):
        super().__init__(coordinate, color, speed, hp)

        self.prey = Grass
        self.state = 'waiting'

    def make_move(self, map) -> None:
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
