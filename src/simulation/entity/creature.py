from abc import abstractmethod

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
# from simulation.entity.grass import Grass
# from simulation.entity.herbivore import Herbivore
# from simulation.entity.predator import Predator
from simulation.pathfinder import Pathfinder

from simulation.game_map import Map

from loguru import logger


class Creature(Entity):
    pathfinder = Pathfinder()

    def __init__(
        self,
        speed: int,
        hp: int,
        prey_class: type[Entity],
        coord: Coordinate = Coordinate(0, 0),
    ):
        self.speed = speed
        self.hp = hp
        self.prey_class = prey_class
        self.coord = coord

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    @abstractmethod
    def make_move(self, game_map: Map) -> None:
        raise NotImplementedError

    def _get_closer(self, path: list[Coordinate], game_map: Map) -> None:
        new_coord = self._get_new_coord(path)
        self._move_to(new_coord, game_map)

    def _get_new_coord(self, path: list[Coordinate]) -> Coordinate:
        nearest_coord_index = len(path) - 2
        try:
            speed_determined_coord_index = path.index(path[self.speed - 1])
            return path[min(speed_determined_coord_index, nearest_coord_index)]
        except IndexError:
            return path[nearest_coord_index]

    def _finish_resource_at(self, coord: Coordinate, game_map: Map) -> None:
        game_map.remove_entity_at(coord)
        logger.info(f'{self} ate {self.prey_class.__name__}')
        self._move_to(coord, game_map)

    def _move_to(self, new_coord: Coordinate, game_map: Map) -> None:
        old_coord = self.coord
        game_map.remove_entity_at(old_coord)
        game_map.add_entity_at(new_coord, self)
        self.coord = new_coord
        logger.info(f'{self} moved from {old_coord.x, old_coord.y} to {new_coord.x, new_coord.y}')
