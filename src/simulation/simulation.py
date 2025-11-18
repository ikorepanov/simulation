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
        self.move_counter = 1
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
        while any(isinstance(entity, (Herbivore, Grass)) for entity in self.game_map.entities.values()):
            logger.info(f'Ход №{self.move_counter}')

            if self.paused:
                self.pause_simulation()

            if not self.running:
                sys.exit()

            self.next_turn()

            self._delay_execution()
            self.move_counter += 1

    def run(self) -> None:
        # запустили второй поток: слушаем инпут от юзера
        t = Thread(target=self.get_and_process_input)
        t.daemon = True
        t.start()

        # расставили сущности на карте
        for action in self.init_actions:
            action.execute(self.game_map)
        self.render_board()
        self._delay_execution()
        logger.info('Все расставлены, всё готово')

        # запустили бесконечный цикл симуляции и рендеринга
        self.start_simulation()

    def pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        logger.info('Симуляция на паузе')

    def render_board(self) -> None:
        self.renderer.render(self.game_map)

    def _delay_execution(self) -> None:
        time.sleep(DELAY_DURATION)

    def _on_event(self) -> None:
        self.render_board()
        self._delay_execution()
