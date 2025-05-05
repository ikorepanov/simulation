from __future__ import annotations

from abc import abstractmethod
from typing import Any, TYPE_CHECKING

from pygame.sprite import AbstractGroup

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
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        sprite_groups = (map.game.creatures,) + (class_specific_groups or ())
        super().__init__(map, color, sprite_groups)

        self.velocity = velocity
        self.hp = hp

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
