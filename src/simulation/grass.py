from __future__ import annotations

from typing import TYPE_CHECKING

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.settings import AMOUNT_OF_GRASS, HEIGHT, TILESIZE, WIDTH, YELLOW


class Grass(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = YELLOW,
    ):
        super().__init__(map, color, (map.game.grass,))

        self.rect.x = WIDTH - TILESIZE  # добавлено на время отладки
        self.rect.y = HEIGHT - TILESIZE  # добавлено на время отладки

        self.amount = AMOUNT_OF_GRASS

    def to_be_eaten(self) -> None:
        pass
