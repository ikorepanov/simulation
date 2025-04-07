from abc import abstractmethod

from simulation.coordinate import Coordinate
from simulation.entity import Entity


class Creature(Entity):
    def __init__(
        self,
        position: Coordinate,
        w: int,
        h: int,
        velocity: int,
        hp: int
    ):
        super().__init__(position, w, h)

        self.velocity = velocity
        self.hp = hp

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
