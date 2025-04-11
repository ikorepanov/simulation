import random

from simulation.coordinate import Abscissa, Coordinate, Ordinate
from simulation.entity import Entity
from simulation.herbivore import Herbivore
from simulation.predator import Predator
from simulation.settings import HEIGHT, HERBIVORE_NUMBER, PREDATOR_NUMBER, TILE, WIDTH


class Map:
    def __init__(
        self,
    ) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.entities: dict[Coordinate, Entity] = {}

    def select_random_value_for_point_on_asix(
        self,
        stop: int,
        start: int = 0,
        step: int = TILE,
    ) -> int:
        return random.randrange(start, stop, step)

    def set_coordinate(
        self,
    ) -> Coordinate:
        attempts = 0
        while attempts < 1000:
            abscissa = Abscissa(self.select_random_value_for_point_on_asix(self.width))
            ordinate = Ordinate(self.select_random_value_for_point_on_asix(self.height))
            coordinate = Coordinate(abscissa=abscissa, ordinate=ordinate)
            if coordinate in self.entities.keys():  # NB! Не работает!
                attempts += 1
                continue
            break
        return coordinate

    def set_entity_on_map(
        self,
        coordinate: Coordinate,
        entity: Entity,
    ) -> None:
        entity.rect.x = coordinate.abscissa.value
        entity.rect.y = coordinate.ordinate.value
        self.entities[coordinate] = entity

    def place_entities_in_init_positions(self) -> None:
        # для первой сущности
        for _ in range(PREDATOR_NUMBER):
            coordinate = self.set_coordinate()
            self.set_entity_on_map(coordinate, Predator(coordinate))
        # для второй сущности
        for _ in range(HERBIVORE_NUMBER):
            coordinate = self.set_coordinate()
            self.set_entity_on_map(coordinate, Herbivore(coordinate))
