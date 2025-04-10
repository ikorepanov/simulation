from simulation.coordinate import Coordinate
from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, HP, TILE, VELOCITY


class Predator(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        w: int = TILE,
        h: int = TILE,
        velocity: int = VELOCITY,
        hp: int = HP,
    ):
        super().__init__(coordinate, w, h, velocity, hp)

        self.attack_power = ATTACK_POWER

    def make_move(self) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass
