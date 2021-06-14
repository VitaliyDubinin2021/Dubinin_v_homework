"""

Task 1 (задание без звездочки - обязательно к выполнению)

"""

with open('nginx_logs.txt') as n:
    data = []
    for line in n:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(data)