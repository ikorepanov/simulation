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
        entity.rect.x = coordinate.abscissa.value
        entity.rect.y = coordinate.ordinate.value
        self.entities[coordinate] = entity

    def set_init_etities_positions(self) -> None:
        pass
