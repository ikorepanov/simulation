# import random
from abc import ABC, abstractmethod

# from simulation.settings import TILESIZE
from simulation.entity.creature import Creature

# from simulation.coordinate import Coordinate
# from simulation.exceptions import NoUnoccupiedTilesError
from simulation.map import Map
from simulation.entity_creator import EntityCreator
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore


class Action(ABC):
    @abstractmethod
    def execute(self, map: Map) -> None:
        raise NotImplementedError


class PlaceEntitiesAction(Action):
    def execute(self, map: Map) -> None:
        creator = EntityCreator()

        coord = map.generate_initial_coordinate()
        entity = creator.create(coord, Grass)
        map.add_entity(coord, entity)

        coord = map.generate_initial_coordinate()
        entity = creator.create(coord, Herbivore)
        map.add_entity(coord, entity)

        # map.setup_initial_entities_positions()


class MoveCreaturesAction(Action):
    def execute(self, map: Map) -> None:
        for coordinate, entitiy in map.entities.items():
            if isinstance(entitiy, Creature):  # need to pass the instance's class, not instance itself
                entitiy.make_move(map)
