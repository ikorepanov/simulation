import sys
import time

from simulation.action import Action
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.game_map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import DELAY_DURATION

from threading import Thread
from loguru import logger


class Simulation:
    def __init__(
            self, game_map: Map, renderer: ConsoleRenderer, init_actions: list[Action], turn_actions: list[Action]
    ) -> None:
        self.game_map = game_map
        self.renderer = renderer
        self.init_actions = init_actions
        self.turn_actions = turn_actions
        self.running = True
        self.paused = False

    def get_and_process_input(self) -> str:
        while True:
            inp = input()
            if inp == 'p':
                logger.info('Simulation is paused')
                self.paused = True
            if inp == 'r':
                logger.info('Simulation is running')
                self.paused = False
            if inp == 'q':
                logger.info('Simulation is finished')
                self.running = False

    def next_turn(self) -> None:
        """Просимулировать и отрендерить один ход."""
        for action in self.turn_actions:
            action.execute(self.game_map)
        self.render_board()

    def start_simulation(self) -> None:
        """Запустить бесконечный цикл симуляции и рендеринга."""
        for action in self.init_actions:
            action.execute(self.game_map)
        self._on_event()

        t = Thread(target=self.get_and_process_input)
        t.daemon = True
        t.start()

        while any(isinstance(entity, (Herbivore, Grass)) for entity in self.game_map.entities.values()):
            if not self.paused:
                self.next_turn()
                self._delay_execution()
            if not self.running:
                sys.exit()

    def pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        self.playing = not self.playing
        if self.playing:
            logger.info('Симуляция возобновлена')
        else:
            logger.info('Симуляция на паузе')

    def render_board(self) -> None:
        self.renderer.render(self.game_map)

    def _delay_execution(self) -> None:
        time.sleep(DELAY_DURATION)

    def _on_event(self) -> None:
        self.render_board()
        self._delay_execution()
