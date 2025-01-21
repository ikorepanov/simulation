from abc import abstractmethod

from simulation.coordinates import Coordinates
from simulation.entity import Entity


class Creature(Entity):
    def __init__(self, coordinates: Coordinates, speed: int, HP: int):
        self.speed = speed
        self.HP = HP
        super().__init__(coordinates)

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
