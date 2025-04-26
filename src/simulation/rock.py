from __future__ import annotations
from typing import TYPE_CHECKING
from simulation.entity import Entity
if TYPE_CHECKING:
    from simulation.map import Map
from simulation.settings import LIGHTGREY


class Rock(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = LIGHTGREY,
    ):
        super().__init__(map, color)
