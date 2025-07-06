from abc import ABC, abstractmethod
from simulation.map_new import Map
import random
from simulation.settings import TILESIZE, NUMBER_OF_ATTEMPTS
from simulation.coordinate import Coordinate


class NoUnoccupiedTilesError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


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

    def generate_initial_coordinate(self, map: Map) -> Coordinate:
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coordinate = Coordinate(
                x=self.pick_random_asix_value(map.width),
                y=self.pick_random_asix_value(map.height)
            )
            if self.is_occupied(coordinate, map):
                attempts += 1
                continue
            return coordinate
        raise NoUnoccupiedTilesError(
            'На карте отсутствуют не занятые клетки. Уменьшите число сущностей или увеличьте размер карты в настройках'
        )

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
