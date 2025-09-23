from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.grass import Grass
from simulation.exceptions import CantFindPathError

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
        try:
            path = Pathfinder().find_path(map, self.coordinate, self.prey)
            print(f'NB! Травоядное нашло путь: {[(node.x, node.y) for node in path]}')
            if len(path) == 1:
                self.eat_grass(path, map)
            else:
                self.move_towards(path, map)
        except CantFindPathError as error:
            print(f"Can't Find Path Error: {error}")
            # sys.exit(1)

    def move_towards(self, path: list[Coordinate], map: Map) -> None:
        entity = map.remove_entity(self.coordinate)
        if map.is_tile_empty(path[self.speed - 1]):
            map.add_entity(path[self.speed - 1], entity)
        self.coordinate = path[self.speed - 1]
        print(f'Травоядное сходило на {self.speed} клетку')

    def eat_grass(self, path: list[Coordinate], map: Map) -> None:
        map.remove_entity(path[0])
        entity = map.remove_entity(self.coordinate)
        map.add_entity(path[0], entity)
        self.coordinate = path[0]
        print('Траврядное съело траву')

    def loose_hp(self) -> None:
        self.hp -= 1
