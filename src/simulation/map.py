from __future__ import annotations

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulation.game import Game

from collections import deque

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

        self.started = False

        self.entities: dict[Coordinate, Entity] = {}

        self.entities_lst = self.create_all_entities()

        # self.start_chasing()

        path = self.get_path_for_resource(Coordinate(0, 0))
        self.print_the_path(path)

    def start_chasing(self) -> None:
        print('NB! The chasing has just started!')
        self.started = True

    def create_all_entities(self) -> list[Entity]:
        entities_lst = []
        for class_name, instance_number in self.entity_set.items():
            for _ in range(instance_number):
                try:
                    entity = class_name(self)
                except NoUnoccupiedTilesError as error:
                    print(f'No Unoccupied Tiles Error: {error.message}')
                    break  # Break the inner loop...
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

    def is_walkable(self, coordinate: Coordinate) -> bool:
        if coordinate in self.entities:
            return False
        return True

    def is_on_map(self, coordinate: Coordinate) -> bool:
        if any(
            [
                coordinate.x < 0,
                coordinate.x >= WIDTH / TILESIZE,
                coordinate.y < 0,
                coordinate.y >= HEIGHT / TILESIZE,
            ]
        ):
            return False
        return True

    def get_all_adjacent(self, coordinate: Coordinate) -> list[Coordinate]:
        adjacent = []
        x = coordinate.x
        y = coordinate.y
        some = [(x + 1, y),  (x, y + 1), (x - 1, y), (x, y - 1)]
        for pair in some:
            coordinate = Coordinate(*pair)
            # if self.is_walkable(coordinate) and self.is_on_map(coordinate):
            if self.is_on_map(coordinate):
                adjacent.append(coordinate)
        return adjacent

    def get_the_path(self, target_node: Coordinate, parents: dict[Coordinate, Coordinate | None]) -> list[Coordinate]:
        some_node: Coordinate | None = target_node
        path = []
        while some_node:
            path.append(some_node)
            some_node = parents[some_node]
        return path

    def get_path_for_resource(self, starting_point: Coordinate) -> list[Coordinate] | None:
        visited: set[Coordinate] = set()
        queue: deque[Coordinate] = deque()
        parents: dict[Coordinate, Coordinate | None] = {}

        queue.appendleft(starting_point)
        parents[starting_point] = None

        while len(queue) > 0:
            node = queue.pop()
            visited.add(node)

            adjacent_nodes = self.get_all_adjacent(node)

            for a_node in adjacent_nodes:
                if a_node in visited or a_node in queue:
                    continue

                queue.appendleft(a_node)
                parents[a_node] = node

                ent = self.entities.get(a_node, None)
                if ent and isinstance(ent, Herbivore):
                    return self.get_the_path(a_node, parents)
        return None

    def print_the_path(self, path: list[Coordinate] | None) -> None:
        some = []
        if path:
            for node in path:
                some.append((node.x, node.y))
        print(f'Путь к цели: {list(reversed(some))}')
