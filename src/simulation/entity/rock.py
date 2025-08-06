from simulation.entity.entity import Entity
from simulation.settings import ROCK


class Rock(Entity):
    def get_sprite(self) -> str:
        return ROCK
