from simulation.entity import Entity
from simulation.settings import PURPLE


class Tree(Entity):
    def __init__(
        self,
        color: tuple[int, int, int] = PURPLE,
    ):

        super().__init__(color)
