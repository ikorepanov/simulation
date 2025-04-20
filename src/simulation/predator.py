from simulation.coordinate import Coordinate
from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, GREEN, HP, VELOCITY


class Predator(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        color: tuple[int, int, int] = GREEN,
        velocity: int = VELOCITY,
        hp: int = HP,
        attack_power: int = ATTACK_POWER
    ):
        super().__init__(coordinate, color, velocity, hp)

        self.attack_power = attack_power

    def make_move(self) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass
