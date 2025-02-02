from abc import ABC, abstractmethod


class Axis(ABC):
    @abstractmethod
    def __init__(
        self,
        value: int,
    ):
        self.value = value
