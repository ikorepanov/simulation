from simulation.coordinate import Coordinate
from simulation.entity import Entity
from simulation.settings import WHITE


class Tree(Entity):
    def __init__(
        self,
        coordinate: Coordinate,
        w: int,
        h: int,
        color: tuple[int, int, int] = WHITE,
    ):
        super().__init__(coordinate, w, h, color)
