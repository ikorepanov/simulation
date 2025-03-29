from simulation.coordinates import Coordinates
from simulation.entity.entity import Entity
from typing import Any
import random
from simulation.params import HEIGHT, TILE, WIDTH
import pygame as pg


class Map:
    def __init__(self) -> None:
        self.entities: dict[Coordinates, Entity] = {}

    def set_entity(self, coordinates: Coordinates, entity: Entity) -> None:
        entity.coordinates = coordinates
        self.entities[coordinates] = entity

    def setup_init_entities_positions(self) -> None:
        pass

    def define_init_entity_coordinates(self) -> Coordinates:
        x = random.randrange(0, WIDTH - TILE + 1, TILE)
        y = random.randrange(0, HEIGHT - TILE + 1, TILE)

        return Coordinates(x, y)

    def create_objects_on_map(self, classes_dict: dict[Any, int]) -> None:
        for class_name, number_of_instances in classes_dict.items():
            for _ in range(number_of_instances):
                coordinates = self.define_init_entity_coordinates()
                self.set_entity(coordinates, class_name(coordinates, TILE, TILE))

    def create_sprites_group(self) -> pg.sprite.Group:
        return pg.sprite.Group()
