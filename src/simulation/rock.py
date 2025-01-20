from simulation.coordinates import Coordinates
from simulation.entity import Entity


class Rock(Entity):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)
