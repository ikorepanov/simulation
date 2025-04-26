from abc import ABC

from simulation.settings import HEIGHT, TILESIZE, WIDTH


class Axis(ABC):
    def __init__(
        self,
        value: int,
        axis_length: int,
    ):
        possible_values = range(int(axis_length / TILESIZE))

        if value in possible_values:
            self.value = possible_values.index(value)

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Axis):
            return NotImplemented
        return (self.value) == (other.value)


class Abscissa(Axis):
    def __init__(
        self,
        value: int,
        axis_length: int = WIDTH,
    ):
        super().__init__(value, axis_length)


class Ordinate(Axis):
    def __init__(
        self,
        value: int,
        axis_length: int = HEIGHT,
    ):
        super().__init__(value, axis_length)


class Coordinate:
    def __init__(
        self,
        abscissa: Abscissa,
        ordinate: Ordinate,
    ):
        self.abscissa = abscissa
        self.ordinate = ordinate

    def __hash__(self) -> int:
        return hash((self.abscissa, self.ordinate))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return (self.abscissa, self.ordinate) == (other.abscissa, other.ordinate)
