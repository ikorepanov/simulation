from simulation.entity import Entity
from simulation.settings import LIGHTGREY


class Rock(Entity):
    def __init__(
        self,
        color: tuple[int, int, int] = LIGHTGREY,
    ):
        super().__init__(color)
