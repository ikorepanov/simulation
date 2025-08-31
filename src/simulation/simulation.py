import sys

from simulation.action import Action, MoveCreaturesAction, PlaceEntitiesAction
from simulation.exceptions import NoUnoccupiedTilesError
from simulation.map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer


class Simulation:
    def __init__(self, map: Map, renderer: ConsoleRenderer) -> None:

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

        # while True:
        #     self.next_turn()
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
        self.start_simulation()
