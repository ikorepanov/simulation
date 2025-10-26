from simulation.coordinate import Coordinate
from simulation.entity.creature import Creature
from simulation.entity.grass import Grass

from simulation.game_map import Map

from loguru import logger

from simulation.entity.entity import Entity
from simulation.settings import HERBIVORE, HERBIVORE_HP, HERBIVORE_SPEED


class Herbivore(Creature):

    def __init__(
        self,
        speed: int = HERBIVORE_SPEED,
        hp: int = HERBIVORE_HP,
        prey: type[Entity] = Grass,
    ):
        super().__init__(speed, hp, prey)

    def get_sprite(self) -> str:
        return HERBIVORE

    def make_move(self, game_map: Map) -> None:
        path = self.pathfinder.find_path(game_map, self.coord, self.prey)  # Ищем путь
        if path:
            if len(path) > 1:  # Далеко
                self.get_closer(path, game_map)  # Приблизиться
            if len(path) == 1:  # Близко
                self.eat(path, game_map)  # Есть
        else:
            # self.wander_or_idle()
            logger.info('Травоядное курит')

    def eat(self, path: list[Coordinate], game_map: Map) -> None:
        self.finish_resource(path, game_map)

    def wander_or_idle(self) -> None:
        pass

    def loose_hp(self, attack_power: int) -> None:
        self.hp -= attack_power
