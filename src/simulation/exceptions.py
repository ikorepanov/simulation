class SimulationError(Exception):
    """Базовый класс для всех исключений в Симуляции."""

    pass


class NoUnoccupiedCoordsError(SimulationError):
    def __init__(self) -> None:
        msg = (
            'There are no unoccupied tiles on the map. '
            'Reduce the number of entities or increase the map size in settings.'
        )
        super().__init__(msg)


class NoPredatorsOnGameMap(SimulationError):
    def __init__(self) -> None:
        msg = (
            'There are no predators on map. '
            'Add at least one in settings (otherwise '
            'there will be no one to eat the herbivores.)'
        )
        super().__init__(msg)
