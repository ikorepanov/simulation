from simulation.entity import Entity
from simulation.map import Map
from simulation.settings import RED


class Rock(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = RED,
    ):
        super().__init__(map, color)
