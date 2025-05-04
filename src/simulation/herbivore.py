from __future__ import annotations

from typing import Any, TYPE_CHECKING

from pygame.sprite import AbstractGroup

from simulation.creature import Creature
from simulation.settings import GREEN, HP, VELOCITY

if TYPE_CHECKING:
    from simulation.map import Map


class Herbivore(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = GREEN,
        velocity: int = VELOCITY,
        hp: int = HP,
        sprite_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        super().__init__(map, color, velocity, hp, sprite_groups or (
            map.game.all_sprites,
            map.game.creatures,
            map.game.herbivores,
            )
        )

    def make_move(self) -> None:
        pass

    def search(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
