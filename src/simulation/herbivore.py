from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.creature import Creature
from simulation.settings import GREEN, HEIGHT, HP, VELOCITY, WIDTH

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.coordinate import Coordinate
from simulation.settings import TILESIZE


class Herbivore(Creature):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = GREEN,
        velocity: int = VELOCITY,
        hp: int = HP,
    ):
        super().__init__(map, color, velocity, hp, (map.game.herbivores,))

        # добавлено на время отладки алгоритма поиска пути
        self.coordinate = Coordinate(WIDTH / TILESIZE - 1, HEIGHT / TILESIZE - 1)
        self.rect.x = self.coordinate.x * TILESIZE
        self.rect.y = self.coordinate.y * TILESIZE

    def make_move(self) -> None:
        pass

    def search(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
