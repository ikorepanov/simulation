from simulation.creature import Creature


class Predator(Creature):
    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        velocity: int,
        hp: int,
        attack_power: int
    ):
        super().__init__(x, y, w, h, velocity, hp)

        self.attack_power = attack_power

    def make_move(self) -> None:
        pass

    def chase(self) -> None:
        pass

    def attack(self) -> None:
        pass
