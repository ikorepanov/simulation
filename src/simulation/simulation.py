import time
from typing import Callable

from simulation.action import Action, MoveAction, PlaceEntitiesAction
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.map import Map
from simulation.renderer.color_schemes import color_scheme
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import COLOR_SCHEME, DELAY_DURATION


class Simulation:
    def __init__(self) -> None:
        self.map = Map()
        self.renderer = ConsoleRenderer(color_scheme[COLOR_SCHEME])

        self.move_action = MoveAction()
        self.register_cb(self.move_action, self.render_and_delay)

        self.place_entities_action = PlaceEntitiesAction()
        self.register_cb(self.place_entities_action, self.render_and_delay)

        self.init_actions = [self.place_entities_action]
        self.turn_actions = [self.move_action]

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

        # while any(isinstance(entity, (Herbivore, Grass)) for entity in self.map.entities.values()):
        while any(isinstance(entity, (Grass)) for entity in self.map.entities.values()):
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
