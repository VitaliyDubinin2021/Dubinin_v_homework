"""

Home Work 8 Task 1 (задание без здездочки - обязательно к выполнению)

"""

import re
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_info = EMAIL.findall(email)[0]
    if found_info:
        name, address = found_info
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, address)

email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')