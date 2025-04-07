from simulation.coordinate import Coordinate
from simulation.entity import Entity


class Map:
    def __init__(
        self,
    ) -> None:
        self.entities: dict[Coordinate, Entity] = {}

    def set_entity(
        self,
        coordinate: Coordinate,
        entity: Entity,
    ) -> None:
        self.entities[coordinate] = entity
        entity.rect.x = coordinate.abscissa.value
        entity.rect.y = coordinate.ordinate.value
