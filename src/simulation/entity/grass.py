from simulation.entity.entity import Entity
from simulation.settings import GRASS


class Grass(Entity):
    pass

    def to_be_eaten(self) -> None:
        pass

    def get_sprite(self) -> str:
        return GRASS
