from simulation.params import GREEN
from simulation.simulation import Simulation


def main() -> None:
    Simulation().start_simulation(GREEN, 'herbivore_small', 'watch_yourself')


if __name__ == '__main__':
    main()
