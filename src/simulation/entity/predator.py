from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.entity.creature import Creature
from simulation.settings import ATTACK_POWER, PREDATOR_HP, PREDATOR_SPEED

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.coordinate import Coordinate
from simulation.entity.herbivore import Herbivore
from simulation.settings import PREDATOR


class Predator(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        speed: int = PREDATOR_SPEED,
        hp: int = PREDATOR_HP,
        attack_power: int = ATTACK_POWER,
    ):
        super().__init__(coordinate, speed, hp)

        self.prey = Herbivore
        self.attack_power = attack_power

    def get_sprite(self) -> str:
        return PREDATOR

    def make_move(self, map: Map) -> None:
        # if self.state == 'moving':
        #     self.move_towards()
        # if self.state == 'eating':
        #     self.attack_prey()
        pass

    def move_towards(self) -> None:
        pass

    def attack_prey(self) -> None:
        pass
