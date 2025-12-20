class SimulationError(Exception):
    """Базовый класс для всех исключений в Симуляции."""


class NoUnoccupiedCoordsError(SimulationError):
    pass


class NoPredatorsOnGameMap(SimulationError):
    pass
