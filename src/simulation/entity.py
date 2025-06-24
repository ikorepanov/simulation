from __future__ import annotations

from typing import Any, TYPE_CHECKING

import pygame
from pygame.sprite import AbstractGroup, Sprite

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.settings import TILESIZE


class Entity(Sprite):  # Абстрактный класс
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int],
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        if class_specific_groups is not None:
            sprite_groups = (map.game.all_sprites,) + (class_specific_groups)
        else:
            sprite_groups = (map.game.all_sprites,)

        super().__init__(*sprite_groups)

        self.map = map
        self.image = pygame.Surface((TILESIZE, TILESIZE))  # Every sprite has to have (1)
        self.image.fill(color)
        self.rect = self.image.get_rect()  # Every sprite has to have (2)

        if not self.map.game.development_mode:
            self.initial_coordinate = self.map.set_initial_coordinate()
            self.rect.x = self.initial_coordinate.x * TILESIZE
            self.rect.y = self.initial_coordinate.y * TILESIZE
