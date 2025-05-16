from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, HP, RED, VELOCITY

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.coordinate import Coordinate
from simulation.settings import TILESIZE


class Predator(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = RED,
        velocity: int = VELOCITY,
        hp: int = HP,
        attack_power: int = ATTACK_POWER,
    ):
        super().__init__(map, color, velocity, hp, (map.game.predators,))

        self.attack_power = attack_power

        # добавлено на время отладки алгоритма поиска пути
        self.coordinate = Coordinate(0, 0)
        self.rect.x = self.coordinate.x * TILESIZE
        self.rect.y = self.coordinate.y * TILESIZE

    def make_move(self) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass
