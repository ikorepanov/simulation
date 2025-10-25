from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.settings import HEIGHT, WIDTH


class Map:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.entities: dict[Coordinate, Entity] = {}

    def is_dark_at(self, coord: Coordinate) -> bool:
        return (coord.x + coord.y) % 2 != 0

    def _has_entity_at(self, coord: Coordinate) -> bool:
        return coord in self.entities

    def is_empty_at(self, coord: Coordinate) -> bool:
        return not self._has_entity_at(coord)

    def is_occupied_at(self, coord: Coordinate) -> bool:
        return self._has_entity_at(coord)

    def add_entity_at(self, coord: Coordinate, entity: Entity) -> None:
        self.entities[coord] = entity

    def get_entity_at(self, coord: Coordinate) -> Entity | None:
        return self.entities.get(coord)

    def remove_entity_at(self, coord: Coordinate) -> Entity:
        return self.entities.pop(coord)

    def is_on_map(self, coord: Coordinate) -> bool:
        return coord.x >= 0 and coord.x < self.width and coord.y >= 0 and coord.y < self.height
