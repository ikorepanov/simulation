from simulation.entity.entity import Entity
from simulation.settings import TREE


class Tree(Entity):
    def get_sprite(self) -> str:
        return TREE
