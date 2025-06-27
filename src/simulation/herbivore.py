from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import HERBIVORE_HP, HERBIVORE_SPEED, TILESIZE, VORTEX

if TYPE_CHECKING:
    from simulation.map import Map

from typing import Any

from pygame.sprite import AbstractGroup

from simulation.coordinate import Coordinate
from simulation.grass import Grass


class Herbivore(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = VORTEX,
        speed: int = HERBIVORE_SPEED,
        hp: int = HERBIVORE_HP,
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        if class_specific_groups is None:
            class_specific_groups = (
                map.game.herbivores,
            )

        super().__init__(map, color, speed, hp, class_specific_groups)

        if self.map.game.development_mode:
            x = 0
            y = 0
            self.coordinate = Coordinate(x, y)
            self.rect.x = self.coordinate.x * TILESIZE
            self.rect.y = self.coordinate.y * TILESIZE

        self.prey = Grass

    def make_move(self) -> None:
        if self.state == 'moving':
            self.move_towards()
        if self.state == 'eating':
            self.eat_grass()

    def move_towards(self) -> None:
        pass

    def eat_grass(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
