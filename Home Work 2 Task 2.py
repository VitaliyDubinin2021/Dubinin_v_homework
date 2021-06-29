"""

Home Work 2 Task 2 (домашнее задание без звездочки - обязательно для выполнения)
Vitaliy Dubinin

"""

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for element in my_list:
    if element.isdigit():
        new_list.extend(['"', f'{int(element):02}', '"'])
    elif (element.startswith('+', 0, 10) or element.startswith('-', 0, 10)) and element[1:].isdigit():
        new_list.extend(['"', f'{element[0]}{int(element[1:]):02}', '"'])
    else:
        new_list.append(element)

out_info = ' '.join(new_list)
print(out_info)
print()

symbols_indexes = []
for index, message in enumerate(out_info):
    if message == '"':
        symbols_indexes.append(index)
print('Индексы символов с кавычками "" ', symbols_indexes)
print()

for index in range(len(symbols_indexes)):
    if index % 2 == 0:
        symbols_indexes[index] = symbols_indexes[index] + 1
    else:
        symbols_indexes[index] = symbols_indexes[index] - 1
print('Индексы символов с пробелами между кавычками "" ', symbols_indexes)
print()

for deleted_indexes in reversed(symbols_indexes):
    out_info = out_info[:deleted_indexes] + out_info[deleted_indexes+1:]
print('Фраза с удаленными пробелами между кавычек "": ', out_info)




