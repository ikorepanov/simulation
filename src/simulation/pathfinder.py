from collections import deque

from simulation.coordinate import Coordinate
from simulation.entity.entity import Entity
from simulation.game_map import Map


class Pathfinder:
    def find_path(self, game_map: Map, start_coord: Coordinate, target_class: type[Entity]) -> list[Coordinate]:
        """
        Запуск алгоритма поиска пути к ближайшей цели

        1. Поместить узел, с которого начинается поиск, в изначально пустую очередь.
        2. Извлечь из начала очереди узел u и пометить его как развёрнутый.
          - Если узел u является целевым узлом, то завершить поиск с результатом «успех».
          - В противном случае, в конец очереди добавляются все преемники узла u, которые ещё не развёрнуты
            и не находятся в очереди.
        3. Если очередь пуста, то все узлы связного графа были просмотрены, следовательно, целевой узел недостижим
           из начального; завершить поиск с результатом «неудача».
        4. Вернуться к п. 2.
        """
        queue: deque[Coordinate] = deque()
        visited: set[Coordinate] = set()
        parents: dict[Coordinate, Coordinate | None] = {}

        queue.appendleft(start_coord)
        parents[start_coord] = None

        while queue:
            coord = queue.pop()
            visited.add(coord)

            if game_map.is_occupied_at(coord) and self._is_entity_of_target_class(game_map, coord, target_class):
                return self._recover_path_from_parents_dict(coord, parents)

            adjacent_coords = self._get_adjacents(game_map, coord)
            available_coords = self._get_available_for_move(game_map, adjacent_coords, target_class)

            for a_coord in available_coords:
                if a_coord in visited or a_coord in queue:
                    continue
                queue.appendleft(a_coord)
                parents[a_coord] = coord

        return []

    def _recover_path_from_parents_dict(
        self,
        target_coord: Coordinate,
        parents: dict[Coordinate, Coordinate | None],
    ) -> list[Coordinate]:
        coord: Coordinate | None = target_coord
        path = []
        while coord:
            path.append(coord)
            coord = parents[coord]
        return path[-2::-1]

    def _get_adjacents(self, game_map: Map, coord: Coordinate) -> list[Coordinate]:
        possible_x_y_pairs = [
            (coord.x + 1, coord.y),
            (coord.x, coord.y + 1),
            (coord.x - 1, coord.y),
            (coord.x, coord.y - 1),
        ]

        return [Coordinate(*pair) for pair in possible_x_y_pairs if game_map.is_on_map(Coordinate(*pair))]

    def _get_available_for_move(self, game_map: Map, adjacents: list[Coordinate], target_class: type[Entity]) -> list[Coordinate]:
        return [
            coord for coord in adjacents
            if game_map.is_empty_at(coord) or self._is_entity_of_target_class(game_map, coord, target_class)
        ]

    def _is_entity_of_target_class(self, game_map: Map, coord: Coordinate, target_class: type[Entity]) -> bool:
        entity = game_map.get_entity_at(coord)
        return isinstance(entity, target_class)
