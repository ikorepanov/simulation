from collections import deque
from simulation.settings import HEIGHT, TILESIZE, WIDTH
from simulation.coordinate import Coordinate
from simulation.map import Map
from simulation.entity import Entity


class Pathfinder:
    def __init__(self, map: Map, init_posititon: Coordinate, target_class: type[Entity]) -> None:
        self.map = map
        self.init_position = init_posititon
        self.target_class = target_class

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
        print(f'NB! {[(node.x, node.y) for node in path[-2:0:-1]]}')
        return path[-2:0:-1]
        # return path[1:-1]

    def find_path(self) -> None:
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

        # current_postition = Coordinate(int(self.rect.x / TILESIZE), int(self.rect.y / TILESIZE))
        queue.appendleft(self.init_position)
        parents[self.init_position] = None

        while queue:
            node = queue.pop()
            visited.add(node)

            if node in self.map.entities and isinstance(self.map.get_entity(node), self.target_class):
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
