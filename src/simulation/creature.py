from __future__ import annotations

from abc import abstractmethod
from typing import Any, TYPE_CHECKING

from pygame.sprite import AbstractGroup

from simulation.entity import Entity

if TYPE_CHECKING:
    from simulation.map import Map

from collections import deque

import pygame

from simulation.coordinate import Coordinate
from simulation.settings import HEIGHT, TILESIZE, WIDTH


class Creature(Entity):
    def __init__(
        self,
        map: Map,
        color: tuple[int, int, int],
        speed: int,  # сколько клеток может пройти за 1 ход
        hp: int,  # Health Points ("здоровье")
        class_specific_groups: tuple[AbstractGroup[Any], ...] | None = None,
    ):
        if class_specific_groups is not None:
            sprite_groups = (map.game.creatures,) + (class_specific_groups)
        else:
            sprite_groups = (map.game.creatures,)

        super().__init__(map, color, class_specific_groups=sprite_groups)

        self.speed = speed
        self.hp = hp

        self.state = 'sniffing'
        self.wait_time = 0
        self.prey: type[Entity] = Entity
        self.path: list[Coordinate] = []
        self.next_node: Coordinate | None = None

    @abstractmethod
    def make_move(self) -> None:
        raise NotImplementedError

    def is_on_map(self, coordinate: Coordinate) -> bool:
        if any(
            [
                coordinate.x < 0,
                coordinate.x >= WIDTH / TILESIZE,
                coordinate.y < 0,
                coordinate.y >= HEIGHT / TILESIZE,
            ]
        ):
            return False
        return True

    def get_adjacents(self, coordinate: Coordinate) -> list[Coordinate]:
        adjacents = []
        x = coordinate.x
        y = coordinate.y
        possible_x_y_pairs = [(x + 1, y),  (x, y + 1), (x - 1, y), (x, y - 1)]
        for pair in possible_x_y_pairs:
            coordinate = Coordinate(*pair)
            if self.is_on_map(coordinate):
                adjacents.append(coordinate)
        return adjacents

    def recover_path_from_parents_dict(
        self,
        target_node: Coordinate,
        parents: dict[Coordinate, Coordinate | None],
    ) -> list[Coordinate]:
        node: Coordinate | None = target_node
        path = []
        while node:
            path.append(node)
            node = parents[node]
        return path[-2:0:-1]
        # return path[1:-1]

    def pick_up_the_scent(self) -> None:
        # Запуск алгоритма поиска пути к ближайшей цели

        # 1. Поместить узел, с которого начинается поиск, в изначально пустую очередь.
        # 2. Извлечь из начала очереди узел u и пометить его как развёрнутый.
        #   - Если узел u является целевым узлом, то завершить поиск с результатом «успех».
        #   - В противном случае, в конец очереди добавляются все преемники узла u, которые ещё не развёрнуты
        #     и не находятся в очереди.
        # 3. Если очередь пуста, то все узлы связного графа были просмотрены, следовательно, целевой узел недостижим
        #    из начального; завершить поиск с результатом «неудача».
        # 4. Вернуться к п. 2.

        visited: set[Coordinate] = set()
        queue: deque[Coordinate] = deque()
        parents: dict[Coordinate, Coordinate | None] = {}

        current_postition = Coordinate(int(self.rect.x / TILESIZE), int(self.rect.y / TILESIZE))
        queue.appendleft(current_postition)
        parents[current_postition] = None

        while queue:
            node = queue.pop()
            visited.add(node)

            if node in self.map.entities and isinstance(self.map.entities.get(node, None), self.prey):
                print('The path has been found')
                self.path = self.recover_path_from_parents_dict(node, parents)
                break

            adjacent_nodes = self.get_adjacents(node)
            for a_node in adjacent_nodes:
                if a_node in visited or a_node in queue:
                    continue
                queue.appendleft(a_node)
                parents[a_node] = node

        else:
            print('Target entities are missing from the map or the path cannot be found')

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
        if self.state == 'sniffing':
            self.pick_up_the_scent()
            if self.path:
                print(f'Path to prey: {[(node.x, node.y) for node in self.path]}')
                self.state = 'checking'  # 'waiting'

        if self.state == 'checking':
            if self.path:
                self.next_node = self.path.pop(0)
                self.state = 'moving'
            else:
                print('STOP')
                self.state = 'stop'

        if self.state == 'moving':
            print(self.next_node.x, self.next_node.y)
            print([(node.x, node.y) for node in self.path])
            if self.next_node:
                if self.rect.x != self.next_node.x * TILESIZE:
                    self.rect.x += self.speed
                    if self.rect.x >= self.next_node.x * TILESIZE:
                        # self.state = 'stop'
                        # self.state = 'waiting'
                        self.state = 'checking'
                        self.wait_time = pygame.time.get_ticks()
                if self.rect.y != self.next_node.y * TILESIZE:
                    self.rect.y += self.speed
                    if self.rect.y >= self.next_node.y * TILESIZE:
                        # self.state = 'stop'
                        # self.state = 'waiting'
                        self.state = 'checking'
                        self.wait_time = pygame.time.get_ticks()

        if self.state == 'stop':
            pass

        if self.state == 'waiting':
            now = pygame.time.get_ticks()
            if now - self.wait_time >= 2000:
                if self.path:
                    self.next_node = self.path.pop(0)
                    self.state = 'moving'
                else:
                    print('STOP')
                    self.state = 'stop'
