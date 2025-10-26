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

    def get_closer(self, path: list[Coordinate], game_map: Map) -> None:
        new_coord = self.get_new_coord(path)
        self.move_to_new_coord(self.coord, new_coord, game_map)

    def get_new_coord(self, path: list[Coordinate]) -> Coordinate:
        nearest_coord_index = len(path) - 2
        try:
            speed_determined_coord_index = path.index(path[self.speed - 1])
            return path[min(speed_determined_coord_index, nearest_coord_index)]
        except IndexError:
            return path[nearest_coord_index]

    def move_to_new_coord(self, old_coord: Coordinate, new_coord: Coordinate, game_map: Map) -> None:
        game_map.remove_entity_at(old_coord)
        game_map.add_entity_at(new_coord, self)
        self.coord = new_coord
        logger.info(f'Крича переместилась с {old_coord.x, old_coord.y} на {new_coord.x, new_coord.y}')

    def finish_resource(self, path: list[Coordinate], game_map: Map) -> None:
        game_map.remove_entity_at(path[0])
        logger.info(f'{self} съел кого-то')
        self.move_to_new_coord(self.coord, path[0], game_map)
