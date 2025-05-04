from __future__ import annotations

from typing import Any, TYPE_CHECKING

import pygame as pg
from pygame.sprite import AbstractGroup, Sprite

from simulation.settings import BLUE, HEIGHT, WIDTH

if TYPE_CHECKING:
    from simulation.game import Game


class Player(Sprite):
    def __init__(
        self,
        game: Game,
    ) -> None:
        self.sprite_groups: AbstractGroup[Any] = game.all_sprites
        super().__init__(self.sprite_groups)

        # image
        self.image = pg.Surface((50, 50))
        self.image.fill(BLUE)

        # rect
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # type: ignore

    def update(self) -> None:
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
