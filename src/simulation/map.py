from simulation.coordinates import Coordinates
from simulation.entity.herbivore import Herbivore


class Map:
    def __init__(self) -> None:
        self.herby_dict: dict[int, Herbivore] = {}

    def create_herby(self, coordinates: Coordinates, speed: int, health: int) -> Herbivore:
        return Herbivore(coordinates, speed, health)

    def create_some_herbivores(self, amount_of_herbies: int) -> dict[int, Herbivore]:
        for number in range(amount_of_herbies):
            x = int(input('Введи координату х: '))
            y = int(input('Введи координату y: '))
            coordinates = Coordinates(x, y)
            speed = int(input('Введи скорость: '))
            health = int(input('Введи уровень здоровя: '))
            herby = self.create_herby(coordinates, speed, health)
            self.herby_dict[number] = herby
        return self.herby_dict
