import pygame as pg

from simulation.settings import HEIGHT, RED, WIDTH


class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        # image
        self.image = pg.Surface((50, 50))
        self.image.fill(RED)

        # rect
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # type: ignore

    def update(self) -> None:
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
