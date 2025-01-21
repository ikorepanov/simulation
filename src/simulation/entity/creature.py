from abc import abstractmethod

from simulation.coordinates import Coordinates
from simulation.entity.entity import Entity


class Creature(Entity):
    def __init__(self, coordinates: Coordinates, speed: int, health: int):
        self.speed = speed
        self.health = health
        super().__init__(coordinates)

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
