from abc import ABC, abstractmethod

from pygame import Surface


class Entity(ABC):
    def __init__(self, window: Surface, x: int, y: int) -> None:
        self.window = window
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self) -> None:  # Сделать не абстрактным (одинаковым для всех)
        raise NotImplementedError


class Creature(Entity):
    def __init__(self, window: Surface, x: int, y: int, speed: int, hp: int) -> None:
        super().__init__(window, x, y)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError
