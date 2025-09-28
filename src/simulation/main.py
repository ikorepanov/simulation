from simulation.map import Map
from simulation.renderer.color_schemes import color_scheme
from simulation.renderer.consolerenderer import ConsoleRenderer
from simulation.settings import COLOR_SCHEME
from simulation.simulation import Simulation


def main() -> None:
    m = Map()
    r = ConsoleRenderer(color_scheme[COLOR_SCHEME])
    s = Simulation(m, r)
    s.start_simulation()


if __name__ == '__main__':
    main()
