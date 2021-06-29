"""

Home Work 10 Task 3 (задание без здездочки - обязательно к выполнению)
Vitaliy Dubinin

"""

class Cage:
    def __init__(self, numbers):
        self.numbers = numbers

    def make_order(self, lines):
        return '\n'.join(['*' * lines for _ in range(self.numbers // lines)]) \
               + '\n' + '*' * (self.numbers % lines)

    def __str__(self):
        return str(self.numbers)

    def __add__(self, other):
        return 'Cумма количества ячеек в двух клетках равна ' + str(self.numbers + other.numbers)

    def __sub__(self, other):
        return self.numbers - other.numbers if self.numbers - other.numbers > 0 \
            else 'Количество ячеек в первой клетке МЕНЬШЕ ЛИБО РАВНО количеству ячеек ' \
                 'во второй клетке, следовательно, найти разность невозможно! '

    def __mul__(self, other):
        return 'Произведение количества ячеек первой и второй клеток равно ' + str(self.numbers * other.numbers)

    def __truediv__(self, other):
        return 'Деление количества ячеек первой и второй клеток равно ' + str(round(self.numbers / other.numbers))

    def __floordiv__(self, other):
        return 'Целочисленное деление количества ячеек первой и второй клеток равно '\
               + str(round(self.numbers / other.numbers))


cage_one = Cage(10)
cage_two = Cage(15)
print('Число ячеек в первой клетке равно', cage_one, 'единиц')
print()
print('Число ячеек во второй клетке равно', cage_two, 'единиц')
print()
print(cage_one + cage_two)
print()
print(cage_one - cage_two)
print()
print(cage_one // cage_two)
print()
print(cage_one / cage_two)
print()
print(cage_two.make_order(10))
print()
print(cage_two.make_order(15))
print()
print(cage_two.make_order(1))
