"""

Home Work 7 Task 4 (обязательно к выполнению - задание без звездочки)

"""

import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dictionary = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dictionary[i] = 0

for file in files:
        out_dictionary[10 ** len(str(file))] += 1

print(out_dictionary)
