from simulation.abscissa import Abscissa
from simulation.ordinate import Ordinate


class Coordinates:
    def __init__(
        self,
        x: int,
        y: int,
    ):
        self.x = Abscissa(x)
        self.y = Ordinate(y)
