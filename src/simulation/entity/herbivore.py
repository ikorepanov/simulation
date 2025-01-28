from simulation.entity.creature import Creature
from simulation.window import Window


class Herbivore(Creature):
    def __init__(
        self,
        window: Window,
        window_width: int,
        window_height: int,
        image_name: str,
    ):
        super().__init__(window, window_width, window_height, image_name)

    def make_move(self) -> None:
        pass
