from __future__ import annotations

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulation.game import Game

from simulation.coordinate import Coordinate
from simulation.entity import Entity
from simulation.grass import Grass
from simulation.herbivore import Herbivore
from simulation.predator import Predator
from simulation.rock import Rock
from simulation.settings import (
    GRASS_NUMBER,
    HEIGHT,
    HERBIVORE_NUMBER,
    NUMBER_OF_ATTEMPTS,
    PREDATOR_NUMBER,
    ROCK_NUMBER,
    TILESIZE,
    TREE_NUMBER,
    WIDTH,
)
from simulation.tree import Tree


class NoUnoccupiedTilesError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class Map:
    def __init__(
        self,
        game: Game,
    ) -> None:
        self.game = game
        self.width = WIDTH
        self.height = HEIGHT

        self.entity_set = {
            Predator: PREDATOR_NUMBER,
            Herbivore: HERBIVORE_NUMBER,
            Rock: ROCK_NUMBER,
            Tree: TREE_NUMBER,
            Grass: GRASS_NUMBER,
        }

        self.entities: dict[Coordinate, Entity] = {}

        self.entities_lst = self.create_all_entities()

    def create_all_entities(self) -> list[Entity]:
        entities_lst = []
        for class_name, instance_number in self.entity_set.items():
            for _ in range(instance_number):
                try:
                    entity = class_name(self)
                except NoUnoccupiedTilesError as error:
                    print(f'No Unoccupied Tiles Error: {error.message}')
                    break  # Break the inner loop...
                self.game.all_sprites.add(entity)
                if class_name in {Predator, Herbivore}:
                    self.game.creatures.add(entity)
                else:
                    self.game.obstacles.add(entity)
                entities_lst.append(entity)
                self.entities[entity.coordinate] = entity
            else:  # "no_break" (continue if the inner loop wasn't broken)
                continue
            break  # Inner loop was broken, break the outer
        return entities_lst

    def select_random_point_on_asix(
        self,
        axis_length: int,  # pixels
    ) -> int:
        return random.randrange(int(axis_length / TILESIZE))  # relative units

    def form_coordinate(self) -> Coordinate:
        x = self.select_random_point_on_asix(self.width)
        y = self.select_random_point_on_asix(self.height)
        return Coordinate(x, y)

    def is_occupied(self, coordinate: Coordinate) -> bool:
        if coordinate in self.entities:
            return True
        return False

    def set_initial_entity_coordinate(self) -> Coordinate:
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coordinate = self.form_coordinate()
            if self.is_occupied(coordinate):
                attempts += 1
                continue
            return coordinate
        raise NoUnoccupiedTilesError(
            'На карте отсутствуют не занятые клетки. Уменьшите число сущностей или увеличьте размер карты в настройках'
        )
