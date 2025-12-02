class Coordinate:
    def __init__(
        self,
        x: int,
        y: int,
    ):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Coordinate {id(self)}'

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)
