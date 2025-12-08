import random
from simulation.entity.entity import Entity
from simulation.settings import GRASS, MAX_GRASS_HEIGHT


class Grass(Entity):
    def __init__(
        self,
        height: int = random.randint(1, MAX_GRASS_HEIGHT),
    ):
        self.height = height

    def __str__(self) -> str:
        return f'Grass, current height: {self.height}'

    def to_be_eaten(self) -> None:
        self.height -= 1

    def to_grow(self) -> None:
        self.height += 1

    def get_sprite(self) -> str:
        return GRASS
