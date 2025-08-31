from collections.abc import Callable

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.rock import Rock


class EntityCreator:
    def create(self, coord: Coordinate, entity_class: type[Entity]) -> Entity:
        creator = get_creator(entity_class)
        return creator(coord)


# some: dict[type[Entity], Callable[[Coordinate], Entity]] = {
#     Herbivore: _create_herbivore,
#     Grass: _create_grass,
#     Rock: _create_rock,
# }


def get_creator(entity_class: type[Entity]) -> Callable[[Coordinate], Entity]:
    if entity_class is Herbivore:
        return _create_herbivore
    elif entity_class is Grass:
        return _create_grass
    elif entity_class is Rock:
        return _create_rock
    else:
        raise ValueError(entity_class)
    # return some[entity_class]


def _create_grass(_coord: Coordinate) -> Grass:
    return Grass()


def _create_herbivore(coord: Coordinate) -> Herbivore:
    return Herbivore(coord)


def _create_rock(_coord: Coordinate) -> Rock:
    return Rock()








def _create_something(**kwargs) -> Entity:
    pass    
