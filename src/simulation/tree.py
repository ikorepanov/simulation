from simulation.coordinates import Coordinates
from simulation.entity import Entity


class Tree(Entity):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)
