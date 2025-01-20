from abc import abstractmethod
from simulation.entity import Entity

from simulation.coordinates import Coordinates


class Creature(Entity):
    def __init__(self, coordinates: Coordinates, speed: int, HP: int):
        self.speed = speed
        self.HP = HP
        super().__init__(coordinates)

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
