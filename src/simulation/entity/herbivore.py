from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.grass import Grass

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.pathfinder import Pathfinder
from simulation.settings import HERBIVORE, HERBIVORE_HP, HERBIVORE_SPEED
from simulation.entity.entity import Entity


class Herbivore(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        speed: int = HERBIVORE_SPEED,
        hp: int = HERBIVORE_HP,
        prey: type[Entity] = Grass,
    ):
        super().__init__(coordinate, speed, hp, prey)

    def get_sprite(self) -> str:
        return HERBIVORE

    def make_move(self, map: Map) -> None:
        path = Pathfinder().find_path(map, self.coordinate, self.prey)
        if path:
            herbivore = map.remove_entity(self.coordinate)
            if len(path) == 1:
                new_coord = path[0]
                # print('Траврядное съело траву')
            else:
                new_coord = path[self.speed - 1]
                # print(f'Травоядное сходило на {self.speed} клетку')
            map.add_entity(new_coord, herbivore)
            self.coordinate = new_coord

    def loose_hp(self) -> None:
        self.hp -= 1
