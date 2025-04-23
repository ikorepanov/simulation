from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map


class Creature(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int],
        velocity: int,
        hp: int,
    ):
        super().__init__(map, color)

        self.velocity = velocity
        self.hp = hp

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
