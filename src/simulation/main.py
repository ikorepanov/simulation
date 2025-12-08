from simulation.action import Action, MoveAction, PlaceEntitiesAction
from simulation.game_map import Map
from simulation.renderer.color_schemes import color_schemes
from simulation.renderer.renderer import Renderer
from simulation.settings import COLOR_SCHEME
from simulation.simulation import Simulation
from simulation.entity_creator import EntityCreator


def main() -> None:
    game_map = Map()

    renderer = Renderer(color_schemes[COLOR_SCHEME])

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
