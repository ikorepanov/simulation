import time
from collections import deque
from threading import Thread

from simulation.action import Action
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.exceptions import NoPredatorsOnGameMap
from simulation.game_map import Map
from simulation.renderer.renderer import Renderer
from simulation.settings import DELAY_DURATION


class Simulation:
    def __init__(
        self,
        game_map: Map,
        renderer: Renderer,
        init_actions: list[Action],
        turn_actions: list[Action],
    ) -> None:
        self.game_map = game_map
        self.move_counter = 1
        self.renderer = renderer
        self.init_actions = init_actions
        self.turn_actions = turn_actions
        self.paused = False
        self.input_queue: deque[str] = deque()

        self._execute_actions(self.init_actions)
        self._run_second_thread()

    def start_simulation(self) -> None:
        self._render_map()
        self._delay_execution()

        if not self.game_map.is_entity_present(Predator):
            raise NoPredatorsOnGameMap()

        self.playing = True
        while self.playing and self.game_map.is_entity_present(Herbivore):
            if self.input_queue:
                self._process_user_input(self.input_queue)
            if not self.paused and self.playing:
                self._next_turn()
                self._count_moves()
                self._delay_execution()

    def _execute_actions(self, actions: list[Action]) -> None:
        for action in actions:
            action.execute(self.game_map)

    def _run_second_thread(self) -> None:
        t = Thread(target=self._get_user_input, args=(self.input_queue,))
        t.daemon = True
        t.start()

    def _render_map(self) -> None:
        self.renderer.render(self.game_map)

    def _delay_execution(self) -> None:
        time.sleep(DELAY_DURATION)

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

    def _count_moves(self) -> None:
        self.move_counter += 1

    def _get_user_input(self, q: deque[str]) -> None:
        while True:
            user_data = input()
            q.append(user_data)

    def _pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        self.paused = not self.paused

    def _quit_simulation(self) -> None:
        if self.playing:
            self.playing = False
