from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.settings import PURPLE


class Tree(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = PURPLE,
    ):
        super().__init__(map, color)
