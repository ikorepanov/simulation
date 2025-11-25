import time

from simulation.action import Action
from simulation.entity.herbivore import Herbivore
from simulation.game_map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import DELAY_DURATION

from threading import Thread
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

        self._execute_actions(self.init_actions)
        self._run_second_thread()

    def _run_second_thread(self) -> None:
        t = Thread(target=self._get_user_input, args=(self.input_queue,))
        t.daemon = True
        t.start()

    def run_game(self) -> None:
        self._render_map()
        self._delay_execution()
        self._start_simulation()

    def _start_simulation(self) -> None:
        # Game Loop
        self.playing = True
        while self.playing and any(isinstance(entity, Herbivore) for entity in self.game_map.entities.values()):
            if self.input_queue:
                self._process_user_input(self.input_queue)
            if not self.paused and self.running:
                self._next_turn()
                self._count_moves()
                self._delay_execution()

    def _get_user_input(self, q: deque[str]) -> None:
        while True:
            user_data = input()
            q.append(user_data)

    def _process_user_input(self, user_input: deque[str]) -> None:
        popped_right = user_input.pop()
        if popped_right == 'p':
            self._pause_simulation()
        elif popped_right == 'q':
            self._quit_simulation()
        user_input.clear()

    def _next_turn(self) -> None:
        """Просимулировать и отрендерить один ход."""
        self._execute_actions(self.turn_actions)
        self._render_map()

    def _pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        self.paused = not self.paused

    def _quit_simulation(self) -> None:
        if self.playing:
            self.playing = False
        self.running = False

    def _render_map(self) -> None:
        self.renderer.render(self.game_map)

    def _delay_execution(self) -> None:
        time.sleep(DELAY_DURATION)

    def _count_moves(self) -> None:
        self.move_counter += 1

    def _execute_actions(self, actions: list[Action]) -> None:
        for action in actions:
            action.execute(self.game_map)
