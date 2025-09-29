from loguru import logger

from simulation.action import MoveAction, PlaceEntitiesAction
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.map import Map
from simulation.renderer.color_schemes import color_scheme
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import COLOR_SCHEME, PAUSE_LENGTH
import time
from simulation.action import Action


class Simulation:
    def __init__(self) -> None:
        self.map = Map()
        self.renderer = ConsoleRenderer(color_scheme[COLOR_SCHEME])

        self.move_action = MoveAction()
        self.move_action.register_callback(self.render_and_pause)

        self.init_actions = [PlaceEntitiesAction()]
        self.turn_actions = [self.move_action]

    def render_board(self) -> None:
        self.renderer.render(self.map)

    def make_pause_after_rendering(self) -> None:
        time.sleep(PAUSE_LENGTH)

    def render_and_pause(self) -> None:
        self.render_board()
        self.make_pause_after_rendering()

    def start_action(self, action: Action, map: Map) -> None:
        action.execute(map)

    def next_turn(self) -> None:
        """Просимулировать и отрендерить один ход."""
        for action in self.turn_actions:
            # action.execute(self.map)
            self.start_action(action, self.map)

    def start_simulation(self) -> None:
        """Запустить бесконечный цикл симуляции и рендеринга."""
        for action in self.init_actions:
            # action.execute(self.map)
            self.start_action(action, self.map)

        self.render_board()
        logger.info('Сущности расставлены')
        time.sleep(0.5)

        while any(isinstance(entity, (Herbivore, Grass)) for entity in self.map.entities.values()):
            self.next_turn()

    def pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        pass
