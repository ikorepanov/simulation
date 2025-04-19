from simulation.coordinate import Coordinate
from simulation.creature import Creature
from simulation.settings import ATTACK_POWER, GREEN, HP, TILESIZE, VELOCITY


class Predator(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        w: int = TILESIZE,
        h: int = TILESIZE,
        color: tuple[int, int, int] = GREEN,
        velocity: int = VELOCITY,
        hp: int = HP,
    ):
        super().__init__(coordinate, w, h, color, velocity, hp)

        self.attack_power = ATTACK_POWER

    def make_move(self) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass
