"""

Home Work 7 Task 3 (обязательно к выполнению - задание без звездочки)

"""

import os
import shutil
my_directory = 'home_work_7_task_3'
if not os.path.exists(my_directory):
    os.mkdir(my_directory)

folder = r'my_project'
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)