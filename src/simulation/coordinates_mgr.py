from simulation.coordinates import Coordinates


class CellsMgr:
    def __init__(
        self,
        max_width: int,
        max_height: int,
        cell_size: int,
    ):
        self.cells: dict[Coordinates, bool] = {}
        for x in range(0, max_width, cell_size):
            for y in range(0, max_height, cell_size):
                self.cells[Coordinates(x, y)] = True
