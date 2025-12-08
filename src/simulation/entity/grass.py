import random
from simulation.entity.entity import Entity
from simulation.settings import GRASS, MAX_GRASS_HEIGHT

from itertools import count


class Grass(Entity):
    _ids = count(1)

    def __init__(
        self,
        height: int = random.randint(1, MAX_GRASS_HEIGHT),
    ):
        super().__init__()

        self.height = height
        self.id = next(self._ids)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}-{self.id} (h.: {self.height})'

    def to_be_eaten(self) -> None:
        self.height -= 1

    def to_grow(self) -> None:
        self.height += 1

    def get_sprite(self) -> str:
        return GRASS
