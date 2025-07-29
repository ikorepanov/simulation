class NoUnoccupiedTilesError(Exception):
    def __init__(self, message: str = 'There are no unoccupied tiles on the map. Reduce the number of entities or increase the map size in settings.'):
        self.message = message
        super().__init__(message)


class CantFindPathError(Exception):
    def __init__(self, message: str = 'Target entities are missing from the map, or the path cannot be found.'):
        super().__init__(message)
