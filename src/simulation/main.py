# import sys

from simulation.renderer.color_schemes import color_scheme

# from simulation.exceptions import NoUnoccupiedTilesError
from simulation.map import Map
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import COLOR_SCHEME
from simulation.simulation import Simulation


def main() -> None:
    m = Map()
    # try:
    #     m.setup_initial_entities_positions()
    # except NoUnoccupiedTilesError as error:
    #     print(f'No Unoccupied Tiles Error: {error.message}')
    #     sys.exit(1)

    s = Simulation(m)
    # s.show_start_screen()

    # while s.running:
    #     s.new()
    #     s.show_go_screen()
    s.new()

    renderer = ConsoleRenderer(color_scheme[COLOR_SCHEME])
    renderer.render(m)


if __name__ == '__main__':
    main()
