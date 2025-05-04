from __future__ import annotations

from typing import Any, TYPE_CHECKING

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from pygame.sprite import AbstractGroup

from simulation.settings import AMOUNT_OF_GRASS, YELLOW


class Grass(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = YELLOW,
        sprite_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        super().__init__(map, color, sprite_groups or (map.game.all_sprites, map.game.grass))

        self.amount = AMOUNT_OF_GRASS

    def to_be_eaten(self) -> None:
        pass
