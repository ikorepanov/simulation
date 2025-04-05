from abc import abstractmethod

from simulation.entity import Entity


class Creature(Entity):
    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        velocity: int,
        hp: int
    ):
        super().__init__(x, y, w, h)

        self.velocity = velocity
        self.hp = hp

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
