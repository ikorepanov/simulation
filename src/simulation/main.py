from simulation.action import Action
from simulation.action import MoveAction, PlaceEntitiesAction
from simulation.map import Map
from simulation.renderer.color_schemes import ColorScheme
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import COLOR_SCHEME
from simulation.simulation import Simulation


def main() -> None:
    m = Map()

    color_scheme = {
        'industrial': ColorScheme(8, 7),
        'midnight': ColorScheme(18, 27),
        'ocean': ColorScheme(4, 12),
        'forest': ColorScheme(2, 10),
        'twilight': ColorScheme(5, 13),
        'glacier': ColorScheme(30, 51),
        'abyss': ColorScheme(23, 66),
    }
    r = ConsoleRenderer(color_scheme[COLOR_SCHEME])

    init_a: list[Action] = [
        PlaceEntitiesAction(),
    ]

    turn_a: list[Action] = [
        MoveAction(),
    ]

    s = Simulation(
        map=m,
        renderer=r,
        init_actions=init_a,
        turn_actions=turn_a,
    )
    s.start_simulation()


if __name__ == '__main__':
    main()
