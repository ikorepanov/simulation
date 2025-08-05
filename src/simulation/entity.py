from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def get_sprite(self) -> str:
        raise NotImplementedError
