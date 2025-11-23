import time

from simulation.action import Action
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.game_map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import DELAY_DURATION

from threading import Thread
from loguru import logger
from collections import deque


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
        self.input_queue: deque[str] = deque()

    def new(self) -> None:
        # start a new game
        self.prepare_simulation()
        self.run_second_thread()
        self.start_simulation()

    def prepare_simulation(self) -> None:
        # расставили сущности на карте
        for action in self.init_actions:
            action.execute(self.game_map)
        self.render_board()
        self._delay_execution()
        logger.info('Все расставлены, всё готово')

    def run_second_thread(self) -> None:
        t = Thread(target=self.get_user_input, args=(self.input_queue,))
        t.daemon = True
        t.start()

    def start_simulation(self) -> None:
        # Game Loop
        self.playing = True
        while self.playing and any(isinstance(entity, (Herbivore, Grass)) for entity in self.game_map.entities.values()):
            if self.input_queue:
                self.process_user_input(self.input_queue)
            if not self.paused and self.running:
                self.next_turn()
                self.count_moves()
                self._delay_execution()

    def get_user_input(self, q: deque[str]) -> None:
        while True:
            user_data = input()
            q.append(user_data)

    def process_user_input(self, user_input: deque[str]) -> None:
        popped_right = user_input.pop()
        if popped_right == 'p':
            self.pause_simulation()
        elif popped_right == 'q':
            self.quit_simulation()
        user_input.clear()

    def next_turn(self) -> None:
        """Просимулировать и отрендерить один ход."""
        for action in self.turn_actions:
            action.execute(self.game_map)
        self.render_board()

    def pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        self.paused = not self.paused

    def quit_simulation(self) -> None:
        if self.playing:
            self.playing = False
        self.running = False

    def render_board(self) -> None:
        self.renderer.render(self.game_map)

    def _delay_execution(self) -> None:
        time.sleep(DELAY_DURATION)

    def count_moves(self) -> None:
        self.move_counter += 1
