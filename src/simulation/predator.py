from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, PREDATOR_SPEED, RED

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.coordinate import Coordinate


class Predator(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = RED,
        speed: int = PREDATOR_SPEED,
        attack_power: int = ATTACK_POWER,
    ):
        super().__init__(map, color, speed, (map.game.predators,))

        self.attack_power = attack_power

    def make_move(self, target_coordinate: Coordinate) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass
