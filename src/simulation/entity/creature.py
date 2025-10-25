from abc import abstractmethod

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.pathfinder import Pathfinder

from simulation.game_map import Map

from loguru import logger


class Creature(Entity):
    pathfinder = Pathfinder()

    def __init__(
        self,
        speed: int,
        hp: int,
        prey: type[Entity],
        coord: Coordinate = Coordinate(0, 0),
    ):
        self.speed = speed
        self.hp = hp
        self.prey = prey
        self.coord = coord

    @abstractmethod
    def make_move(self, game_map: Map) -> None:
        raise NotImplementedError

    def get_new_coord(self, path: list[Coordinate]) -> Coordinate:
        index_1 = path.index(path[self.speed - 1])
        index_2 = len(path) - 2
        return path[min(index_1, index_2)]

    def occupy_new_position(self, old_coord: Coordinate, new_coord: Coordinate, game_map: Map) -> None:
        entity = game_map.remove_entity_at(old_coord)
        game_map.add_entity_at(new_coord, entity)
        self.coord = new_coord

    def get_exact_same_coord(self, coord: Coordinate, game_map: Map) -> Coordinate:  # Надо этот метод убирать (раз уж hash и eq у нас переопределены...)
        for obj in game_map.entities.keys():
            if obj.x == coord.x and obj.y == coord.y:
                return obj
        return coord  # ?
        # return [obj for obj in game_map.entities.keys() if obj.x == coord.x and obj.y == coord.y]

    def finish_resource(self, path: list[Coordinate], game_map: Map) -> None:
        prey_coord = self.get_exact_same_coord(path[0], game_map)
        game_map.remove_entity_at(path[0])
        self.occupy_new_position(self.coord, prey_coord, game_map)
        logger.info(f'{self} съел кого-то')
