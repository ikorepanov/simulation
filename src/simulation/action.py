# import random
from abc import ABC, abstractmethod

# from simulation.coordinate import Coordinate
# from simulation.exceptions import NoUnoccupiedTilesError
from simulation.map import Map
# from simulation.settings import TILESIZE
from simulation.creature import Creature


class Action(ABC):
    def __init__(self, map: Map) -> None:
        self.map = map

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class PlaceEntitiesAction(Action):
    def __init__(self, map: Map) -> None:
        super().__init__(map)

    def execute(self) -> None:
        self.map.setup_initial_entities_positions()


class MoveCreaturesAction(Action):
    def __init__(self, map: Map) -> None:
        super().__init__(map)

    def execute(self) -> None:
        for coordinate, entitiy in self.map.entities.items():
            if isinstance(entitiy, Creature):  # need to pass the instance's class, not instance itself
                entitiy.make_move(self.map)
