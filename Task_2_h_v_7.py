"""

Задание №2: Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

"""

from random import randint as ri

customer_number = int(input('Здравствуйте! Укажите размерность массива (для удобноства не более 15 элементов): '))


def sorting(our_array):
    if len(our_array) < 2:
        return our_array

    array_middle = len(our_array) // 2

    left_before_middle = our_array[:array_middle]
    right_after_middle = our_array[array_middle:]

    left_before_middle = sorting(left_before_middle)
    right_after_middle = sorting(right_after_middle)

    return return_part(left_before_middle, right_after_middle)


def return_part(array_one, array_two):
    x = 0
    y = 0
    our_res = []
    while len(array_one) > x and len(array_two) > y:
        if array_two[y] >= array_one[x]:
            our_res.append(array_one[x])
            x += 1
        else:
            our_res.append(array_two[y])
            y += 1

    our_res += array_one[x:]
    our_res += array_two[y:]

    return our_res


numbers_for_result = [ri(0, 49) for _ in range(customer_number)]

print(f'Изначально массив, сформированный из случайных чисел указанного диапазона, '
      f'выглядит следующим образом: {numbers_for_result}')

print(f'Остортированный по возрастанию по методу слияния массив принимает '
      f'следующий вид: {sorting(numbers_for_result)}')
