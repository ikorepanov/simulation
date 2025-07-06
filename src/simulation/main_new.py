import pygame

from simulation.map_new import Map
from simulation.simulation import Simulation

import sys


class NoUnoccupiedTilesError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def main() -> None:
    m = Map()
    try:
        m.setup_initial_entities_positions()
    except NoUnoccupiedTilesError as error:
        print(f'No Unoccupied Tiles Error: {error.message}')
        pygame.quit()
        sys.exit(1)

    s = Simulation(m)
    s.show_start_screen()

    while s.running:
        s.new()
        s.show_go_screen()

    pygame.quit()


if __name__ == '__main__':
    main()
