from __future__ import annotations

from typing import Any, TYPE_CHECKING

from pygame.sprite import AbstractGroup

from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, HP, RED, VELOCITY

if TYPE_CHECKING:
    from simulation.map import Map


class Predator(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = RED,
        velocity: int = VELOCITY,
        hp: int = HP,
        attack_power: int = ATTACK_POWER,
        sprite_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):

        super().__init__(map, color, velocity, hp, sprite_groups or (
            map.game.all_sprites,
            map.game.creatures,
            map.game.predators,
            )
        )

        self.attack_power = attack_power

    def make_move(self) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass
