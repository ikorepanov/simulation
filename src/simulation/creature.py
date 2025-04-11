from abc import abstractmethod

from simulation.coordinate import Coordinate
from simulation.entity import Entity


class Creature(Entity):
    def __init__(
        self,
        coordinate: Coordinate,
        w: int,
        h: int,
        color: tuple[int, int, int],
        velocity: int,
        hp: int,
    ):
        super().__init__(coordinate, w, h, color)

        self.velocity = velocity
        self.hp = hp

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
