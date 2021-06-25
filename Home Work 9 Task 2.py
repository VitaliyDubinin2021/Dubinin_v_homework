"""

Dubinin Vitaliy
Home Work 9 Task 2 (задание без звездочки - обязательно к выполнению)

"""

class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calculate_asphalt_mass(self):
        asphalt_mass = self._length * self._width * 25 * 5 / 1000
        return asphalt_mass

my_road = Road(25, 6000)
print(my_road.calculate_asphalt_mass(), 'тонн асфальта потребуется!!!')