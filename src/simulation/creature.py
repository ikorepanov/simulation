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
        sprite_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        super().__init__(map, color, sprite_groups or (map.game.all_sprites, map.game.creatures))

        self.velocity = velocity
        self.hp = hp

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
