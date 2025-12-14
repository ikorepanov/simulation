from simulation.entity.entity import Entity
from simulation.settings import ROCK_SPRITE


class Rock(Entity):
    def get_sprite(self) -> str:
        return ROCK_SPRITE
