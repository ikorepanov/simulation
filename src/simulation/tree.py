from simulation.coordinate import Coordinate
from simulation.entity import Entity


class Tree(Entity):
    def __init__(
        self,
        coordinate: Coordinate,
        w: int,
        h: int,
    ):
        super().__init__(coordinate, w, h)
