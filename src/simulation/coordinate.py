from simulation.settings import WIDTH, HEIGHT


class Coordinate:
    def __init__(
        self,
        x: int,
        y: int,
    ):
        # try:
        self.x = x  # relative units
        self.y = y  # relative units
        # except Exception as error:
        #     print("You're trying to use wrong value: {error}.")

    # def check_value(self, value):
    #     if value >= WIDTH:
    #         raise Exception

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)
