from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from typing import Any

from pygame.sprite import AbstractGroup

from simulation.coordinate import Coordinate
from simulation.settings import AMOUNT_OF_GRASS, HEIGHT, MINTWAVE, TILESIZE, WIDTH


class Grass(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = MINTWAVE,
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
        amount: int = AMOUNT_OF_GRASS,
    ):
        if class_specific_groups is None:
            class_specific_groups = (
                map.game.grass,
            )

        super().__init__(map, color, class_specific_groups)

        self.amount = amount

        if self.map.game.development_mode:
            x = int((WIDTH - TILESIZE) / TILESIZE)
            y = int((HEIGHT - TILESIZE) / TILESIZE)
            self.initial_coordinate = Coordinate(x, y)
            self.rect.x = self.initial_coordinate.x * TILESIZE
            self.rect.y = self.initial_coordinate.y * TILESIZE

    def to_be_eaten(self) -> None:
        pass
