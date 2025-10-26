from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.grass import Grass

from simulation.game_map import Map

from loguru import logger

from simulation.settings import HERBIVORE, HERBIVORE_HP, HERBIVORE_SPEED


class Herbivore(Creature):

    def __init__(
        self,
        speed: int = HERBIVORE_SPEED,
        hp: int = HERBIVORE_HP,
        prey_class: type[Grass] = Grass,
    ):
        super().__init__(speed, hp, prey_class)

    def get_sprite(self) -> str:
        return HERBIVORE

    def make_move(self, game_map: Map) -> None:
        path = self.pathfinder.find_path(game_map, self.coord, self.prey_class)
        if path:
            if len(path) > 1:
                self._get_closer(path, game_map)
            if len(path) == 1:
                self._eat_at(path[0], game_map)
        else:
            # self.wander_or_idle()
            logger.info('Травоядное курит')

    def _eat_at(self, coord: Coordinate, game_map: Map) -> None:
        self._finish_resource_at(coord, game_map)

    def _wander_or_idle(self) -> None:
        pass

    def _loose_hp(self, attack_power: int) -> None:
        self.hp -= attack_power
