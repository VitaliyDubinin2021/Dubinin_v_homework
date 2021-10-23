"""

Задание №3: Массив размером 2m + 1, где m – натуральное число, заполнен
случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда,
делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если
это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

"""

from random import randint as ri

m = int(input('Здравствуйте! Введите значение коэффициента m для формулы "2 * m + 1": '))


def our_median(our_half, length):
    if len(length) == 1:
        return length[0]
    if len(length) == 0:
        return 0

    points = []
    point = length[0]

    more_than = []
    less_than = []

    for u in length:
        if u < point:
            less_than.append(u)
        elif u > point:
            more_than.append(u)
        else:
            points.append(u)

    if len(less_than) > our_half:
        return our_median(our_half, less_than)
    elif our_half < (len(points) + len(less_than)):
        return points[0]
    else:
        return our_median(our_half - len(more_than) - len(points), more_than)


custom_array = [ri(-111, 111) for _ in range(2 * m + 1)]

print(f'Массив в исходном состоянии принимает следующий вид {custom_array}')
print(f'Медиана массива {custom_array} - элемент массива со значением {our_median(m, custom_array)}')




