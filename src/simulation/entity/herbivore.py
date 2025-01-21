from simulation.coordinates import Coordinates
from simulation.entity.creature import Creature


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int, health: int):
        super().__init__(coordinates, speed, health)

    def make_move(self) -> None:
        pass
