"""

Task 3 (задание без звездочки - обязательно к исполнению)

"""

from itertools import zip_longest
import json
my_dict = {}
with open('users.csv', encoding='utf-8') as users_name:
    with open('hobby.csv', encoding='utf-8') as users_hobby:
        num_lines_users = sum(1 for line in users_name)
        num_lines_hobby = sum(1 for line in users_hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        users_name.seek(0)
        users_hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(users_name, users_hobby):
            my_dict[line_user.strip()] = line_user_hobby.strip() if \
                line_user_hobby is not None else line_user_hobby

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)
print(my_dict)


