import sys
from typing import Any


from simulation.action import Action, MoveCreaturesAction, PlaceEntitiesAction
from simulation.exceptions import NoUnoccupiedTilesError

from simulation.map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.entity_creator import EntityCreator


class Simulation:
    def __init__(self, map: Map, renderer: ConsoleRenderer) -> None:
        self.running = True

        self.map = map
        self.renderer = renderer

        self.init_actions: list[Action] = [PlaceEntitiesAction()]
        self.turn_actions: list[Action] = [MoveCreaturesAction()]

    def next_turn(self) -> None:
        """Просимулировать и отрендерить один ход."""

        for action in self.turn_actions:
            action.execute(self.map)

    def start_simulation(self) -> None:
        """Запустить бесконечный цикл симуляции и рендеринга."""

        while True:
            self.next_turn()

    def pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""

        pass

    def new(self) -> None:
        # Start a new game (reset the game, not the whole program)
        for action in self.init_actions:
            try:
                action.execute(self.map)
            except NoUnoccupiedTilesError as error:
                print(f'No Unoccupied Tiles Error: {error.message}')
                sys.exit(1)

        self.renderer.render(self.map)

        # self.next_turn()

        ############
        # coordinates = []

        # for coordinate, obj in self.map.entities.items():
        #     if isinstance(obj, Herbivore):
        #         coordinates.append(coordinate)
        #     else:
        #         continue

        # from simulation.pathfinder import Pathfinder
        # Pathfinder(
        #     self.map,
        #     coordinates[0],
        #     Grass,
        # ).find_path()
        #############

        # ***********
        # for key, val in self.map.entities.items():
        #     if isinstance(val, Herbivore):
        #         available_tiles = [
        #             (coordinate.x, coordinate.y) for coordinate in val.get_available_move_tiles(self.map)
        #         ]
        #         print(f'NB! Available Tiles: {available_tiles}')
        # ***********

        self.run()

    def run(self) -> None:
        self.playing = True
        # while self.playing:
            # бесконечный цикл симуляции?

    def show_start_screen(self) -> None:
        # Game splash/start screen
        pass

    def show_go_screen(self) -> None:
        # Game over/continue
        pass
