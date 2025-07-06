import random
from abc import ABC, abstractmethod

from simulation.coordinate import Coordinate
from simulation.exceptions import NoUnoccupiedTilesError
from simulation.map import Map
from simulation.settings import TILESIZE


class Action(ABC):
    @abstractmethod
    def execute(self, map: Map) -> None:
        raise NotImplementedError


class PlaceEntitiesAction(Action):
    def pick_random_asix_value(
        self,
        axis_length: int,  # pixels
    ) -> int:
        return random.randrange(int(axis_length / TILESIZE))  # relative units

    def is_occupied(self, coordinate: Coordinate, map: Map) -> bool:
        if coordinate in map.entities:
            return True
        return False

    # def generate_initial_coordinate(self, map: Map) -> Coordinate:
    #     attempts = 0
    #     while attempts < NUMBER_OF_ATTEMPTS:
    #         coordinate = Coordinate(
    #             x=self.pick_random_asix_value(map.width),
    #             y=self.pick_random_asix_value(map.height)
    #         )
    #         if self.is_occupied(coordinate, map):
    #             attempts += 1
    #             continue
    #         return coordinate
    #     raise NoUnoccupiedTilesError(
    #         'There are no unoccupied tiles on the map. Reduce the number of entities or increase the map size '
    #         'in settings.'
    #     )

    def execute(self, map: Map) -> None:
        for entity in ...:
            try:
                coordinate = self.generate_initial_coordinate(map)
            except NoUnoccupiedTilesError as error:
                print(f'No Unoccupied Tiles Error: {error.message}')
                break
            map.entities[coordinate] = entity


class MoveCreaturesAction(Action):
    def execute(self, map: Map) -> None:
        for creature in map.creatures:
            creature.make_move()
