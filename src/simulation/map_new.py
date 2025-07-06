import random

from simulation.coordinate import Coordinate
from simulation.creature import Creature
from simulation.entity import Entity
from simulation.exceptions import NoUnoccupiedTilesError
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

CLASSES_TO_CREATE: dict[type[Entity], int] = {
    Predator: PREDATOR_NUMBER,
    Herbivore: HERBIVORE_NUMBER,
    Rock: ROCK_NUMBER,
    Tree: TREE_NUMBER,
    Grass: GRASS_NUMBER,
}


class Map:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.entities: dict[Coordinate, Entity] = {}

    def add_entity(self, coordinate: Coordinate, entity: Entity) -> None:
        # if isinstance(entity, Creature):
        #     entity.coordinate = coordinate
        self.entities[coordinate] = entity

    def pick_random_asix_value(
        self,
        axis_length: int,  # pixels
    ) -> int:
        return random.randrange(int(axis_length / TILESIZE))  # relative units

    def is_tile_occupied(self, coordinate: Coordinate) -> bool:
        if coordinate in self.entities:
            return True
        return False

    def generate_initial_coordinate(self) -> Coordinate:
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coordinate = Coordinate(
                x=self.pick_random_asix_value(self.width),
                y=self.pick_random_asix_value(self.height)
            )
            if self.is_tile_occupied(coordinate):
                attempts += 1
                continue
            return coordinate
        raise NoUnoccupiedTilesError(
            'There are no unoccupied tiles on the map. Reduce the number of entities or increase the map size '
            'in settings.'
        )

    def setup_initial_entities_positions(self) -> None:
        for class_name, instance_number in CLASSES_TO_CREATE.items():
            for _ in range(instance_number):
                coordinate = self.generate_initial_coordinate()

                if issubclass(class_name, Creature):
                    self.add_entity(
                        coordinate=coordinate,
                        entity=class_name(coordinate),  # type: ignore
                    )
                else:
                    entity = class_name()  # type: ignore
                    self.add_entity(
                        coordinate=coordinate,
                        entity=entity,
                    )
                    entity.place_rect_on_corresponding_coordinate(coordinate.x, coordinate.y)

    def get_entity(self, coordinate: Coordinate) -> Entity | None:
        return self.entities.get(coordinate)

    def get_list_of_entities(self) -> list[tuple[tuple[int, int], Entity]]:
        return [((coordinate.x, coordinate.y), entity) for coordinate, entity in self.entities.items()]

    def remove_entity(self) -> None:
        pass
