from __future__ import annotations

from abc import abstractmethod

from simulation.coordinate import Coordinate
from simulation.entity import Entity
from simulation.settings import TILESIZE


class Creature(Entity):
    def __init__(
        self,
        coordinate: Coordinate,
        color: tuple[int, int, int],
        speed: int,  # сколько клеток может пройти за 1 ход
        hp: int,  # Health Points ("здоровье")
    ):
        super().__init__(color)

        # "... координата нужна только тому существу, которое ходит.
        # Поэтому entities должны хранить координату только начиная с уровня Creature."
        self.coordinate = coordinate
        self.rect.x = self.coordinate.x * TILESIZE
        self.rect.y = self.coordinate.y * TILESIZE
        self.speed = speed
        self.hp = hp

        # self.state = 'sniffing'
        # self.wait_time = 0
        # self.prey: type[Entity] = Entity
        # self.path: list[Coordinate] = []
        # self.next_node: Coordinate | None = None

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError

    def check_if_movement_is_possible(self) -> bool:
        # Проверить - возможно ли "шагнуть" на ту или иную клетку
        is_possible: bool
        return is_possible

    def check_if_collide(self) -> bool:
        # Проверяем, приблизились ли вплотную к цели
        is_collide: bool
        return is_collide

    def act_as_intendent(self) -> None:
        # Атаковать - для хищников, есть (траву) - для травоядных
        pass

    def update(self) -> None:
        pass
        # if self.state == 'sniffing':
        #     self.pick_up_the_scent()
        #     if self.path:
        #         print(f'Path to prey: {[(node.x, node.y) for node in self.path]}')
        #         self.state = 'checking'  # 'waiting'

        # if self.state == 'checking':
        #     if self.path:
        #         self.next_node = self.path.pop(0)
        #         self.state = 'moving'
        #     else:
        #         print('STOP')
        #         self.state = 'stop'

        # if self.state == 'moving':
        #     print(self.next_node.x, self.next_node.y)
        #     print([(node.x, node.y) for node in self.path])
        #     if self.next_node:
        #         if self.rect.x != self.next_node.x * TILESIZE:
        #             self.rect.x += self.speed
        #             if self.rect.x >= self.next_node.x * TILESIZE:
        #                 # self.state = 'stop'
        #                 # self.state = 'waiting'
        #                 self.state = 'checking'
        #                 self.wait_time = pygame.time.get_ticks()
        #         if self.rect.y != self.next_node.y * TILESIZE:
        #             self.rect.y += self.speed
        #             if self.rect.y >= self.next_node.y * TILESIZE:
        #                 # self.state = 'stop'
        #                 # self.state = 'waiting'
        #                 self.state = 'checking'
        #                 self.wait_time = pygame.time.get_ticks()

        # if self.state == 'stop':
        #     pass

        # if self.state == 'waiting':
        #     now = pygame.time.get_ticks()
        #     if now - self.wait_time >= 2000:
        #         if self.path:
        #             self.next_node = self.path.pop(0)
        #             self.state = 'moving'
        #         else:
        #             print('STOP')
        #             self.state = 'stop'
