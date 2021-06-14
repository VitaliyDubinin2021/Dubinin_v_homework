"""

Task 2 (* задание со звездочкой - необязательно к исполнению)

"""

with open('nginx_logs.txt') as n:
    data = []
    spamer_dict = {}
    for line in n:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spamer_dict.setdefault(splitted[0], 0)
        spamer_dict[splitted[0]] += 1

spamer_dict = sorted(spamer_dict.items(), key=lambda p: p[1], reverse=True)
print(spamer_dict[:10])