from __future__ import annotations

from abc import ABC
from typing import Any, TYPE_CHECKING

import pygame as pg
from pygame.sprite import AbstractGroup, Sprite

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.settings import TILESIZE


class Entity(Sprite, ABC):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int],
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
        w: int = TILESIZE,
        h: int = TILESIZE,
    ):
        sprite_groups = (map.game.all_sprites,) + (class_specific_groups or ())
        super().__init__(*sprite_groups)

        self.map = map
        self.image = pg.Surface((w, h))  # Every sprite has to have (1)
        self.image.fill(color)
        self.rect = self.image.get_rect()  # Every sprite has to have (2)
        self.coordinate = self.map.set_initial_entity_coordinate()
        self.rect.x = self.coordinate.x * TILESIZE
        self.rect.y = self.coordinate.y * TILESIZE

    def update(self) -> None:
        pass
