import time
from itertools import chain
# from typing import Callable

from simulation.action import Action
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import DELAY_DURATION


class Simulation:
    def __init__(
            self, map: Map, renderer: ConsoleRenderer, init_actions: list[Action], turn_actions: list[Action]
    ) -> None:
        self.map = map
        self.renderer = renderer
        self.init_actions = init_actions
        self.turn_actions = turn_actions

        for action in chain(self.init_actions, self.turn_actions):
            action.register_callback(self._on_event)

    def next_turn(self) -> None:
        """Просимулировать и отрендерить один ход."""
        for action in self.turn_actions:
            action.execute(self.map)

    def start_simulation(self) -> None:
        """Запустить бесконечный цикл симуляции и рендеринга."""
        for action in self.init_actions:
            action.execute(self.map)

        while any(isinstance(entity, (Herbivore, Grass)) for entity in self.map.entities.values()):
            self.next_turn()

    def pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        pass

    def render_board(self) -> None:
        self.renderer.render(self.map)

    def _delay_execution(self) -> None:
        time.sleep(DELAY_DURATION)

    def _on_event(self) -> None:
        self.render_board()
        self._delay_execution()
