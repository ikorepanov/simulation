from abc import ABC

from simulation.settings import HEIGHT, TILESIZE, WIDTH


class Axis(ABC):
    def __init__(
        self,
        value: int,
        axis_length: int,
        tile_size: int,
    ):
        possible_values = range(0, axis_length, tile_size)
        if value in possible_values:
            # self.value = possible_values.index(value)
            self.value = value

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
        tile_size: int = TILESIZE,
    ):
        super().__init__(value, axis_length, tile_size)


class Ordinate(Axis):
    def __init__(
        self,
        value: int,
        axis_length: int = HEIGHT,
        tile_size: int = TILESIZE,
    ):
        super().__init__(value, axis_length, tile_size)


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
