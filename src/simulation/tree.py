from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from typing import Any

from pygame.sprite import AbstractGroup

from simulation.settings import PURPLE


class Tree(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = PURPLE,
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        if class_specific_groups is None:
            class_specific_groups = (
                map.game.obstacles,
                map.game.trees,
            )

        super().__init__(map, color, class_specific_groups)
