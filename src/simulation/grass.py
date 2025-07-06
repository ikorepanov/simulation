from __future__ import annotations

from simulation.entity import Entity
from simulation.settings import AMOUNT_OF_GRASS, MINTWAVE


class Grass(Entity):
    def __init__(
        self,
        color: tuple[int, int, int] = MINTWAVE,
        amount: int = AMOUNT_OF_GRASS,
    ):
        super().__init__(color)

        self.amount = amount

    def to_be_eaten(self) -> None:
        pass
