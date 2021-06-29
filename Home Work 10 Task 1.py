"""

Home Work 10 Task 1 (задание без здездочки - обязательно к выполнению)
Vitaliy Dubinin

"""

class Matrix:
    def __init__(self, input_date):
        self.input = input_date

    def __str__(self):
        return '\n' . join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_one, line_two in zip(self.input, other.input):
                if len(line_one) != len(line_two):
                    return 'Возникли проблемы с отображением!!!'

                summed_lines = [x + y for x, y in zip(line_one, line_two)]
                answer += ' '.join(map(str, summed_lines)) + '\n'

        else:
            return 'Возникли проблемы с отображением!!!'
        return answer


matrix_one = Matrix([[2, 5], [3, 8], [1, 5], [4, 9]])
matrix_two = Matrix([[5, 6], [2, 3], [1, 2], [4, 9]])
print('Первая матрица')
print(matrix_one)
print()
print('Вторая матрица')
print(matrix_two)
print()
print('Сумма первой и второй матриц')
print(matrix_one + matrix_two)



