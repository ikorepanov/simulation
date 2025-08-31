import random

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.exceptions import NoUnoccupiedTilesError
from simulation.settings import HEIGHT, NUMBER_OF_ATTEMPTS, WIDTH


class Map:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.entities: dict[Coordinate, Entity] = {}

    def is_tile_dark(self, coordinate: Coordinate) -> bool:
        return (coordinate.x + coordinate.y) % 2 != 0

    def add_entity(self, coordinate: Coordinate, entity: Entity) -> None:
        self.entities[coordinate] = entity

    def is_tile_empty(self, coordinate: Coordinate) -> bool:
        return coordinate not in self.entities

    def generate_initial_coordinate(self) -> Coordinate:  # Возможно - перенести в другой класс (Action?)
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coordinate = Coordinate(
                x=random.randrange(self.width),
                y=random.randrange(self.height)
            )
            if not self.is_tile_empty(coordinate):
                attempts += 1
                continue
            return coordinate
        raise NoUnoccupiedTilesError()

    def get_entity(self, coordinate: Coordinate) -> Entity | None:
        return self.entities.get(coordinate)

    def remove_entity(self) -> None:
        pass
