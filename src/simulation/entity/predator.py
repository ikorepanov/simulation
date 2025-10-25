from simulation.entity.creature import Creature
from simulation.settings import ATTACK_POWER, PREDATOR_HP, PREDATOR_SPEED

from simulation.game_map import Map

from loguru import logger

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.entity.herbivore import Herbivore
from simulation.pathfinder import Pathfinder
from simulation.settings import PREDATOR


class Predator(Creature):
    def __init__(
        self,
        speed: int = PREDATOR_SPEED,
        hp: int = PREDATOR_HP,
        prey: type[Entity] = Herbivore,
        attack_power: int = ATTACK_POWER,
    ):
        super().__init__(speed, hp, prey)

        self.attack_power = attack_power

    def get_sprite(self) -> str:
        return PREDATOR

    def make_move(self, game_map: Map) -> None:
        path = Pathfinder().find_path(game_map, self.coord, self.prey)  # Ищем путь
        if len(path) > 1:  # Далеко
            self.get_closer(path, game_map)  # Приблизиться
        if len(path) == 1:  # Близко
            self.attack(path, game_map)  # Атаковать

    def get_closer(self, path: list[Coordinate], game_map: Map) -> None:
        new_coord = self.new_coord(path)
        self.occupy_new_position(self.coord, new_coord, game_map)
        logger.info(f'Хищник сходил на {self.speed} клетку')

    def bite(self, prey: Herbivore, attack_power: int) -> None:
        prey.loose_hp(attack_power)

    def is_done(self, prey: Herbivore) -> bool:
        return prey.hp <= 0

    def attack(self, path: list[Coordinate], game_map: Map) -> None:
        herbivore = game_map.get_entity_at(path[0])
        if isinstance(herbivore, Herbivore):
            self.bite(herbivore, self.attack_power)
            if self.is_done(herbivore):
                self.finish_resource(path, game_map)
                # game_map.remove_entity(path[0])  # NB!!! Надо как-то использовать ранее полученного herbivore для этого...
                # self.occupy_new_position(self.coord, path[0], game_map)
            else:
                logger.info('Хищник укусил травоядное')
