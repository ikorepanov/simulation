from simulation.entity import Entity
from simulation.map import Map
from simulation.settings import AMOUNT_OF_GRASS, YELLOW


class Grass(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int] = YELLOW,
    ):
        super().__init__(map, color)

        self.amount = AMOUNT_OF_GRASS

    def to_be_eaten(self) -> None:
        pass
