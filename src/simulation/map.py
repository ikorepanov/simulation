import random

from simulation.coordinate import Abscissa, Coordinate, Ordinate
from simulation.entity import Entity
from simulation.settings import ATTEMPTS, HEIGHT, TILE, WIDTH


class MyException(Exception):
    pass


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
        while attempts < ATTEMPTS:
            abscissa = Abscissa(self.select_random_value_for_point_on_asix(self.width))
            ordinate = Ordinate(self.select_random_value_for_point_on_asix(self.height))
            coordinate = Coordinate(abscissa=abscissa, ordinate=ordinate)
            if coordinate in self.entities:
                attempts += 1
                continue
            return coordinate
        raise MyException(
            'На карте отсутствуют не занятые клетки. Уменьшите число существ или увеличьте размер карты в настройках'
        )

    def set_entity_on_map(
        self,
        coordinate: Coordinate,
        entity: Entity,
    ) -> None:
        entity.rect.x = coordinate.abscissa.value
        entity.rect.y = coordinate.ordinate.value
        self.entities[coordinate] = entity

    def place_entities_in_init_positions(
        self,
        some_volume: dict[type[Entity], int],
    ) -> None:
        for class_name, instance_number in some_volume.items():
            for _ in range(instance_number):
                try:
                    coordinate = self.set_coordinate()
                except MyException as error:
                    print(error)
                    break  # Break the inner loop...
                self.set_entity_on_map(coordinate, class_name(coordinate))  # type: ignore
            else:  # "no_break" (continue if the inner loop wasn't broken)
                continue
            break  # Inner loop was broken, break the outer
