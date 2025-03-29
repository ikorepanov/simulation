from abc import ABC


class Axis(ABC):
    def __init__(
        self,
        value: int,
    ):
        self.value = value
