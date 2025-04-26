from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, RED, HP, VELOCITY

if TYPE_CHECKING:
    from simulation.map import Map


class Predator(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = RED,
        velocity: int = VELOCITY,
        hp: int = HP,
        attack_power: int = ATTACK_POWER
    ):

        super().__init__(map, color, velocity, hp)

        self.attack_power = attack_power

    def make_move(self) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass
