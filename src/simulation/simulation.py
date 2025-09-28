from simulation.action import Action, MoveCreaturesAction, PlaceEntitiesAction
from simulation.map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore


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
        for action in self.init_actions:
            action.execute(self.map)

        self.renderer.render(self.map)

        while any(isinstance(entity, (Herbivore, Grass)) for entity in self.map.entities.values()):
            self.next_turn()

    def pause_simulation(self) -> None:
        """Приостановить бесконечный цикл симуляции и рендеринга."""
        pass
