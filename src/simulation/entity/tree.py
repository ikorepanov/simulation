from simulation.entity.entity import Entity
from simulation.settings import TREE_SPRITE


class Tree(Entity):
    def get_sprite(self) -> str:
        return TREE_SPRITE
