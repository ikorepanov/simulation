from __future__ import annotations

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulation.game import Game

from simulation.coordinate import Abscissa, Coordinate, Ordinate
from simulation.entity import Entity
from simulation.predator import Predator
from simulation.settings import ATTEMPTS, HEIGHT, PREDATOR_NUMBER, TILESIZE, WIDTH


class MyException(Exception):
    pass


class Map:
    def __init__(
        self,
        game: Game,
    ) -> None:
        self.game = game
        self.width = WIDTH
        self.height = HEIGHT
        self.entities: dict[Coordinate, Entity] = {}
        self.predators = self.create_predators()

    def create_predators(self) -> list[Predator]:
        lst = []
        for i in range(PREDATOR_NUMBER):
            p = Predator(self)
            self.game.all_sprites.add(p)
            self.game.creatures.add(p)
            lst.append(p)
        return lst

    def select_random_value_for_point_on_asix(
        self,
        stop: int,
        start: int = 0,
        step: int = TILESIZE,
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

    # def set_entity_on_map(
    #     self,
    #     coordinate: Coordinate,
    #     entity: Entity,
    # ) -> None:
    #     entity.rect.x = coordinate.abscissa.value
    #     entity.rect.y = coordinate.ordinate.value
    #     self.entities[coordinate] = entity

    # def place_entities_in_init_positions(
    #     self,
    #     some_volume: dict[type[Entity], int],
    # ) -> None:
    #     for class_name, instance_number in some_volume.items():
    #         for _ in range(instance_number):
    #             try:
    #                 coordinate = self.set_coordinate()
    #             except MyException as error:
    #                 print(error)
    #                 break  # Break the inner loop...
    #             self.set_entity_on_map(coordinate, class_name(coordinate))  # type: ignore
    #         else:  # "no_break" (continue if the inner loop wasn't broken)
    #             continue
    #         break  # Inner loop was broken, break the outer
