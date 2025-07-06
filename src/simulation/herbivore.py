from __future__ import annotations

from simulation.coordinate import Coordinate
from simulation.creature import Creature
from simulation.grass import Grass
from simulation.settings import HERBIVORE_HP, HERBIVORE_SPEED, VORTEX


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

    def make_move(self) -> None:
        if self.state == 'moving':
            self.move_towards()
        if self.state == 'eating':
            self.eat_grass()

    def move_towards(self) -> None:
        pass

    def eat_grass(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
