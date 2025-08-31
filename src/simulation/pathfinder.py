from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

from simulation.coordinate import Coordinate
from simulation.settings import HEIGHT, WIDTH

if TYPE_CHECKING:
    from simulation.map import Map

from simulation.entity.entity import Entity
from simulation.exceptions import CantFindPathError


class Pathfinder:
    def is_on_map(self, coordinate: Coordinate) -> bool:
        if any(
            [
                coordinate.x < 0,
                coordinate.x >= WIDTH,
                coordinate.y < 0,
                coordinate.y >= HEIGHT,
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
        return path[-2::-1]

    def find_path(self, map: Map, init_position: Coordinate, target_class: type[Entity]) -> list[Coordinate]:
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

        queue.appendleft(init_position)
        parents[init_position] = None

        while queue:
            node = queue.pop()
            visited.add(node)

            if node in map.entities and isinstance(map.get_entity(node), target_class):
                return self.recover_path_from_parents_dict(node, parents)

            adjacent_nodes = self.get_adjacents(node)
            for a_node in adjacent_nodes:
                if a_node in visited or a_node in queue:
                    continue
                queue.appendleft(a_node)
                parents[a_node] = node

        else:
            raise CantFindPathError()
