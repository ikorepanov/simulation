from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, HP, RED, VELOCITY

if TYPE_CHECKING:
    from simulation.map import Map

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

        self.target_x = self.coordinate.x + 1
        self.show_target_coordinate()

    def make_move(self) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass

    def update(self) -> None:
        self.speed_x = 0
        if self.map.started:
            self.speed_x = 1
            if self.rect.x >= self.target_x * TILESIZE:
                self.speed_x = 0
                self.map.started = False
        self.rect.x += self.speed_x

    def show_target_coordinate(self) -> None:
        print(f'Target X: {self.target_x}')
