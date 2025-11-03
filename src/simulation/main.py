from simulation.action import Action, MoveAction, PlaceEntitiesAction
from simulation.game_map import Map
from simulation.renderer.color_schemes import ColorScheme
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import COLOR_SCHEME
from simulation.simulation import Simulation
from simulation.entity_creator import EntityCreator


def main() -> None:
    game_map = Map()

    color_scheme = {
        'industrial': ColorScheme(8, 7),
        'midnight': ColorScheme(18, 27),
        'ocean': ColorScheme(4, 12),
        'forest': ColorScheme(2, 10),
        'twilight': ColorScheme(5, 13),
        'glacier': ColorScheme(30, 51),
        'abyss': ColorScheme(23, 66),
    }
    renderer = ConsoleRenderer(color_scheme[COLOR_SCHEME])

    entity_creator = EntityCreator()

    init_actions: list[Action] = [
        PlaceEntitiesAction(entity_creator.run()),
    ]

    turn_actions: list[Action] = [
        MoveAction(),
    ]

    simulation = Simulation(
        game_map=game_map,
        renderer=renderer,
        init_actions=init_actions,
        turn_actions=turn_actions,
    )
    simulation.start_simulation()


if __name__ == '__main__':
    main()
