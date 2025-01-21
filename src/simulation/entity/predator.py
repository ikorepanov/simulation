from simulation.coordinates import Coordinates
from simulation.entity.creature import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int, health: int, attack_power: int):
        self.attack_power = attack_power
        super().__init__(coordinates, speed, health)

    def make_move(self) -> None:
        pass
