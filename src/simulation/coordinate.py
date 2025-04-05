from abc import ABC

from simulation.settings import HEIGHT, TILE, WIDTH


class Axis(ABC):
    def __init__(
        self,
        value: int,
        axis_length: int,
        tile_size: int,
    ):
        possible_values = range(0, axis_length, tile_size)
        if value in possible_values:
            self.value = possible_values.index(value)


class Abscissa(Axis):
    def __init__(
        self,
        value: int,
        axis_length: int = WIDTH,
        tile_size: int = TILE,
    ):
        super().__init__(value, axis_length, tile_size)


class Ordinate(Axis):
    def __init__(
        self,
        value: int,
        axis_length: int = HEIGHT,
        tile_size: int = TILE,
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
