from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.coordinate import Coordinate
from simulation.settings import AMOUNT_OF_GRASS, HEIGHT, MINTWAVE, TILESIZE, WIDTH


class Grass(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = MINTWAVE,
    ):
        super().__init__(map, color, (map.game.grass,))

        if self.map.game.development_mode:
            x = int((WIDTH - TILESIZE) / TILESIZE)
            y = int((HEIGHT - TILESIZE) / TILESIZE)
            self.coordinate = Coordinate(x, y)
            self.rect.x = self.coordinate.x * TILESIZE
            self.rect.y = self.coordinate.y * TILESIZE

        self.amount = AMOUNT_OF_GRASS

    def to_be_eaten(self) -> None:
        pass
