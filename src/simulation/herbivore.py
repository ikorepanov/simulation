from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import GREEN, HP, VELOCITY

if TYPE_CHECKING:
    from simulation.map import Map


class Herbivore(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = GREEN,
        velocity: int = VELOCITY,
        hp: int = HP,
    ):
        super().__init__(map, color, velocity, hp)

    def make_move(self) -> None:
        pass

    def search(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
