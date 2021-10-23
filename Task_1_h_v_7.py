"""

Задание №1: Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный
случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный
массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

"""

from random import randint as ri
from timeit import timeit as ti


def sorting_by_bubble(our_array):
    for x in range(len(our_array) - 1, 0, -1):
        flag_our_point = True
        for y in range(x):
            if our_array[y] >= our_array[y + 1]:
                our_array[y], our_array[y + 1] = our_array[y + 1], our_array[y]
                flag_our_point = False

        if flag_our_point == True:
            break
    return our_array


numb_of_range = int(input('Здравствуйте! Введите какое количество цифр должно составлять формируемый массив при '
                          'двух реализациях алгоритма: '))
our_random_numbers = [ri(-100, 99) for _ in range(numb_of_range)]
print(f'Первоначальный вид массива до сортировки: {our_random_numbers}')

print(f'Массив после сортировки при первой реализации, сформированный из случайных чисел из указанного '
      f'диапазона: {sorting_by_bubble(our_random_numbers)}')

# Второй вариант реализации данного алгоритма:


def sorting_by_bubble_second_realisation(second_array):
    for i in range(len(second_array) - 1, 0, -1):
        for j in range(i):
            if second_array[j] >= second_array[j + 1]:
                second_array[j], second_array[j + 1] = second_array[j + 1], second_array[j]

    return second_array


print(f'Массив после сортировки при второй реализации, сформированный из случайных чисел из указанного диапазона: '
      f'{sorting_by_bubble_second_realisation(our_random_numbers)}')

# Теперь сравним скорость выполнения первой и второй реализаций алгоритма сортировки массива из случайных чисел
# указанного диапазона!

number_iterations = 100

time_first_realisation = ti(f'sorting_by_bubble({our_random_numbers})',
                            setup='from __main__ import sorting_by_bubble',
                            number=number_iterations)

time_second_realisation = ti(f'sorting_by_bubble_second_realisation({our_random_numbers})',
                            setup='from __main__ import sorting_by_bubble_second_realisation',
                            number=number_iterations)

print(f'Время выполнения первой реализации алгоритма: {time_first_realisation} секунд')
print(f'Время выполнения первой реализации алгоритма: {time_second_realisation} секунд')
print(f'Первый алгоритм работает быстрее, чем второй в {round(time_second_realisation/time_second_realisation, 10)} '
      f'раз/раза !')
print(f'Вывод: обе реализации алгоритма работают примерно одинаково быстро (очень быстро - доли секунды), программный '
      f'код первой реализации алгоритма более громоздкий, чем у второй!')












