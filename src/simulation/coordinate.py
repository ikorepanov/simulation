
from __future__ import annotations

from simulation.coordinate_shift import CoordinateShift
from simulation.settings import HEIGHT, TILESIZE, WIDTH


class Coordinate:
    def __init__(
        self,
        x: int,
        y: int,
    ):
        self.x = x  # relative units
        self.y = y  # relative units

    def __repr__(self) -> str:
        return f'Coordinate {id(self)}'

    def shift(self, shift: CoordinateShift) -> Coordinate:
        return Coordinate(self.x + shift.x_shift, self.y + shift.y_shift)

    def can_shift(self, shift: CoordinateShift) -> bool:
        x = self.x + shift.x_shift
        y = self.y + shift.y_shift

        if x < 0 or x > (WIDTH - TILESIZE) / TILESIZE:
            return False

        if y < 0 or y > (HEIGHT - TILESIZE) / TILESIZE:
            return False

        return True

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)
