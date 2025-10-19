from simulation.action import Action, MoveAction, PlaceEntitiesAction
from simulation.entity.entity import Entity
from simulation.entity.grass import Grass
from simulation.entity.herbivore import Herbivore
from simulation.entity.predator import Predator
from simulation.entity.rock import Rock
from simulation.entity.tree import Tree
from simulation.map import Map
from simulation.renderer.color_schemes import ColorScheme
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import COLOR_SCHEME, GRASS_NUMBER, HERBIVORE_NUMBER, PREDATOR_NUMBER, ROCK_NUMBER, TREE_NUMBER
from simulation.simulation import Simulation


def main() -> None:
    map = Map()

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

    entity_instance_counts: dict[type[Entity], int] = {
        Predator: PREDATOR_NUMBER,
        Herbivore: HERBIVORE_NUMBER,
        Rock: ROCK_NUMBER,
        Tree: TREE_NUMBER,
        Grass: GRASS_NUMBER,
    }

    entities = []
    for cls, count in entity_instance_counts.items():
        for _ in range(count):
            entities.append(cls())

    init_actions: list[Action] = [
        PlaceEntitiesAction(entities),
    ]

    turn_actions: list[Action] = [
        MoveAction(),
    ]

    simulation = Simulation(
        map=map,
        renderer=renderer,
        init_actions=init_actions,
        turn_actions=turn_actions,
    )
    simulation.start_simulation()


if __name__ == '__main__':
    main()
