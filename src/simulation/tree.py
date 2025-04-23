from simulation.entity import Entity
from simulation.map import Map
from simulation.settings import WHITE


class Tree(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = WHITE,
    ):
        super().__init__(map, color)
