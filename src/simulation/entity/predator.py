from simulation.entity.creature import Creature
from simulation.settings import ATTACK_POWER, PREDATOR_HP, PREDATOR_SPEED

from simulation.game_map import Map

from loguru import logger

from simulation.coordinate import Coordinate
from simulation.entity.herbivore import Herbivore
from simulation.pathfinder import Pathfinder
from simulation.settings import PREDATOR


class Predator(Creature):
    def __init__(
        self,
        speed: int = PREDATOR_SPEED,
        hp: int = PREDATOR_HP,
        prey_class: type[Herbivore] = Herbivore,
        attack_power: int = ATTACK_POWER,
    ):
        super().__init__(speed, hp, prey_class)

        self.attack_power = attack_power
        self.prev_coords: list[Coordinate] = []

    def get_sprite(self) -> str:
        return PREDATOR

    def make_move(self, game_map: Map) -> None:
        if self.is_in_circles():
            logger.info('Умный хищник остаётся на месте')
            self.prev_coords.clear()
            pass
        else:
            path = Pathfinder().find_path(game_map, self.coord, self.prey_class)
            if len(path) > 1:
                self.prev_coords.append(self.coord)
                if len(self.prev_coords) > 4:
                    self.prev_coords.pop(0)
                self._get_closer(path, game_map)
            if len(path) == 1:
                self._attack_at(path[0], game_map)

    def is_in_circles(self) -> bool:
        # print([(coord.x, coord.y) for coord in self.prev_coords])
        if len(self.prev_coords) > 3:
            logger.info(f'In circles: { self.prev_coords[0] == self.prev_coords[2] and self.prev_coords[1] == self.prev_coords[3]}')
            return self.prev_coords[0] == self.prev_coords[2] and self.prev_coords[1] == self.prev_coords[3]
        else:
            return False

    def stay(self) -> None:
        pass

    def _attack_at(self, coord: Coordinate, game_map: Map) -> None:
        entity = game_map.get_entity_at(coord)
        if isinstance(entity, self.prey_class):
            entity._loose_hp(self.attack_power)
            self._finish_resource_at(coord, game_map) if entity.hp == 0 else logger.info('Хищник укусил травоядное')
            # if entity.hp == 0:
            #     self._finish_resource_at(coord, game_map)
