from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import GREEN, HERBIVORE_SPEED

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.coordinate import Coordinate


class Herbivore(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = GREEN,
        speed: int = HERBIVORE_SPEED,
    ):
        super().__init__(map, color, speed, (map.game.herbivores,))

        self.rect.x = 0  # добавлено на время отладки
        self.rect.y = 0  # добавлено на время отладки

    def make_move(self, target_coordinate: Coordinate) -> None:
        pass

    def search(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
