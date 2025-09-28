from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.settings import HEIGHT, WIDTH


class Map:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.entities: dict[Coordinate, Entity] = {}

    def is_tile_dark(self, coordinate: Coordinate) -> bool:
        return (coordinate.x + coordinate.y) % 2 != 0

    def is_tile_empty(self, coordinate: Coordinate) -> bool:
        return coordinate not in self.entities

    def add_entity(self, coordinate: Coordinate, entity: Entity) -> None:
        self.entities[coordinate] = entity

    def get_entity(self, coordinate: Coordinate) -> Entity:
        # return self.entities.get(coordinate)
        return self.entities[coordinate]

    def remove_entity(self, coordinate: Coordinate) -> Entity:
        return self.entities.pop(coordinate)
