"""

Home Work 7 Task 1 (обязательно к выполнению - задание без звездочки)

"""

import os

sample = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in sample.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            current_directory = os.path.join(root, folder)
            if os.path.exists(current_directory):
                print(cur_dir, 'существует')
            else:
                os.makedirs(current_directory)