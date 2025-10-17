import time
from typing import Callable

from simulation.action import Action
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import DELAY_DURATION

from itertools import chain


class Simulation:
    def __init__(self, map: Map, renderer: ConsoleRenderer, init_actions: list[Action], turn_actions: list[Action]) -> None:
        self.map = map
        self.renderer = renderer
        self.init_actions = init_actions
        self.turn_actions = turn_actions

        for action in chain(self.init_actions, self.turn_actions):
            self.register_cb(action, self.render_and_delay)

    def launch_action(self, action: Action) -> None:
        action.execute(self.map)

    def next_turn(self) -> None:
        """Просимулировать и отрендерить один ход."""
        for action in self.turn_actions:
            self.launch_action(action)

    def start_simulation(self) -> None:
        """Запустить бесконечный цикл симуляции и рендеринга."""
        for action in self.init_actions:
            self.launch_action(action)

        while any(isinstance(entity, (Herbivore, Grass)) for entity in self.map.entities.values()):
            self.next_turn()

    def pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        pass

    def render_board(self) -> None:
        self.renderer.render(self.map)

    def delay_execution(self) -> None:
        time.sleep(DELAY_DURATION)

    def render_and_delay(self) -> None:
        self.render_board()
        self.delay_execution()

    def register_cb(self, action: Action, fn: Callable[..., None]) -> None:
        action.register_callback(fn)
