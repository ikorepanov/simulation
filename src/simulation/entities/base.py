from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):  # Сделать не абстрактным, а одинаковым для всех (обычным)
        raise NotImplementedError


class Creature(Entity):
    def __init__(self, window, x, y, speed, hp):
        super().__init__(window, x, y)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self):
        raise NotImplementedError
