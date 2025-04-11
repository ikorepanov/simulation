from simulation.coordinate import Coordinate
from simulation.entity import Entity
from simulation.settings import AMOUNT_OF_GRASS, YELLOW


class Grass(Entity):
    def __init__(
        self,
        coordinate: Coordinate,
        w: int,
        h: int,
        color: tuple[int, int, int] = YELLOW,
    ):
        super().__init__(coordinate, w, h, color)

        self.amount = AMOUNT_OF_GRASS

    def to_be_eaten(self) -> None:
        pass
