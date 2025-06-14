from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import HERBIVORE_SPEED, TILESIZE, VORTEX

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.coordinate import Coordinate
from simulation.grass import Grass


class Herbivore(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = VORTEX,
        speed: int = HERBIVORE_SPEED,
    ):
        super().__init__(map, color, speed, (map.game.herbivores,))

        if self.map.game.development_mode:
            x = 0
            y = 0
            self.coordinate = Coordinate(x, y)
            self.rect.x = self.coordinate.x * TILESIZE
            self.rect.y = self.coordinate.y * TILESIZE

        self.prey = Grass

    def make_move(self, target_coordinate: Coordinate) -> None:
        pass

    def search(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
