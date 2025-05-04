from __future__ import annotations

from typing import Any, TYPE_CHECKING

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from pygame.sprite import AbstractGroup

from simulation.settings import LIGHTGREY


class Rock(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = LIGHTGREY,
        sprite_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        super().__init__(map, color, sprite_groups or (map.game.all_sprites, map.game.obstacles, map.game.rocks))
