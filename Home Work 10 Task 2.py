"""

Home Work 10 Task 2 (задание без здездочки - обязательно к выполнению)
Vitaliy Dubinin

"""

from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, parametr):
        self.parametr = parametr

    @abstractmethod
    def calculator(self):
        pass


class OverCoat(Clothing):

    @property
    def calculator(self):
        return round(0.5 + (self.parametr / 6.5))


class Costume(Clothing):

    @property
    def calculator(self):
        return round(0.3 + (2 * self.parametr))


over_coat = OverCoat(55)
costume = Costume(185)
print(over_coat.calculator)
print(costume.calculator)
