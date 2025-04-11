from simulation.coordinate import Coordinate
from simulation.creature import Creature
from simulation.settings import BLUE, HP, TILE, VELOCITY


class Herbivore(Creature):
    def __init__(
        self,
        coordinate: Coordinate,
        w: int = TILE,
        h: int = TILE,
        color: tuple[int, int, int] = BLUE,
        velocity: int = VELOCITY,
        hp: int = HP,
    ):
        super().__init__(coordinate, w, h, color, velocity, hp)

    def make_move(self) -> None:
        pass

    def search(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def loose_hp(self) -> None:
        pass
