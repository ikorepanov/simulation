from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, PREDATOR_HP, PREDATOR_SPEED, RED

if TYPE_CHECKING:
    from simulation.map import Map

from typing import Any

from pygame.sprite import AbstractGroup

from simulation.herbivore import Herbivore


class Predator(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = RED,
        speed: int = PREDATOR_SPEED,
        hp: int = PREDATOR_HP,
        attack_power: int = ATTACK_POWER,
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        if class_specific_groups is None:
            class_specific_groups = (
                map.game.predators,
            )

        super().__init__(map, color, speed, hp, class_specific_groups)

        self.prey = Herbivore
        self.attack_power = attack_power

    def make_move(self) -> None:
        if self.state == 'moving':
            self.move_towards()
        if self.state == 'eating':
            self.attack_prey()

    def move_towards(self) -> None:
        pass

    def attack_prey(self) -> None:
        pass
