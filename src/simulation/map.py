import random

from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.entity import Entity
from simulation.exceptions import NoUnoccupiedTilesError
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.rock import Rock
from simulation.settings import (
    GRASS_NUMBER,
    HEIGHT,
    HERBIVORE_NUMBER,
    NUMBER_OF_ATTEMPTS,
    PREDATOR_NUMBER,
    ROCK_NUMBER,
    TREE_NUMBER,
    WIDTH,
)
from simulation.entity.tree import Tree

entites_to_create: dict[type[Entity], int] = {  # NB! Это надо перенести в - предположительно - action (которое init).
    Predator: PREDATOR_NUMBER,  # Там же создавать сущности (а не в map, как сейчас). А затем вызывать методы map только
    Herbivore: HERBIVORE_NUMBER,  # для генерации случайной координаты и добавленя сущности на карту
    Rock: ROCK_NUMBER,  # (в словать entities)
    Tree: TREE_NUMBER,
    Grass: GRASS_NUMBER,
}


class Map:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.entities: dict[Coordinate, Entity] = {}

    def is_tile_dark(self, coordinate: Coordinate) -> bool:
        return (coordinate.x + coordinate.y) % 2 != 0

    def add_entity(self, coordinate: Coordinate, entity: Entity) -> None:
        # Только Creature могут двигать => могут знать свою координату
        # if isinstance(entity, Creature):
        #     entity.coordinate = coordinate
        self.entities[coordinate] = entity

    # @staticmethod
    # def pick_random_asix_value(
    #     axis_length: int,  # pixels
    # ) -> int:
    #     return random.randrange(int(axis_length / TILESIZE))  # relative units

    # def is_tile_occupied(self, coordinate: Coordinate) -> bool:
    #     if coordinate in self.entities:
    #         return True
    #     return False

    def is_tile_empty(self, coordinate: Coordinate) -> bool:
        return coordinate not in self.entities

    def generate_initial_coordinate(self) -> Coordinate:
        attempts = 0
        while attempts < NUMBER_OF_ATTEMPTS:
            coordinate = Coordinate(
                x=random.randrange(self.width),
                y=random.randrange(self.height)
            )
            if not self.is_tile_empty(coordinate):
                attempts += 1
                continue
            return coordinate
        raise NoUnoccupiedTilesError()

    def setup_initial_entities_positions(self) -> None:
        # for class_name, instance_number in CLASSES_TO_CREATE.items():
        #     for _ in range(instance_number):
        #         coordinate = self.generate_initial_coordinate()

        #         if issubclass(class_name, Creature):
        #             self.add_entity(
        #                 coordinate=coordinate,
        #                 entity=class_name(coordinate),  # type: ignore
        #             )
        #         else:
        #             entity = class_name()
        #             self.add_entity(
        #                 coordinate=coordinate,
        #                 entity=entity,
        #             )

        # for _ in range(HERBIVORE_NUMBER):
        #     coord = self.generate_initial_coordinate()
        #     entity = Herbivore(coord)
        #     self.add_entity(coord, entity)

        # for _ in range(GRASS_NUMBER):
        #     coord = self.generate_initial_coordinate()
        #     entity = Grass()
        #     self.add_entity(coord, entity)

        for class_name, number_of_entities in entites_to_create.items():
            for _ in range(number_of_entities):
                coord = self.generate_initial_coordinate()
                entity = class_name(coord) if issubclass(class_name, Creature) else class_name()  # type: ignore
                self.add_entity(coord, entity)

    def get_entity(self, coordinate: Coordinate) -> Entity | None:
        return self.entities.get(coordinate)

    # def get_list_of_entities(self) -> list[tuple[tuple[int, int], Entity]]:
    #     return [((coordinate.x, coordinate.y), entity) for coordinate, entity in self.entities.items()]

    def remove_entity(self) -> None:
        pass

# if is_subclass(class_name, Creature):
#     entity = class_name(coord)
# else:
#     entity = class_name()

# entity = class_name(coord) if is_subclass(class_name, Creature) else class_name()
