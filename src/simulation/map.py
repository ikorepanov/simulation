from simulation.coordinates import Coordinates
from simulation.entity.entity import Entity


class Map():
    def __init__(self, coordinates: Coordinates, entity: Entity):
        self.some = {coordinates: entity}

    def set_entites(self, coordinates: Coordinates, entity: Entity) -> None:
        entity.coordinates = coordinates
        ...

    def setup_start_entity_positions(self) -> None:  # Первоначальная расстановка сущностей по карте
        pass
