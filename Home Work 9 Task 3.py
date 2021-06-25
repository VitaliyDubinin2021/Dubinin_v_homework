"""

Dubinin Vitaliy
Home Work 9 Task 3 (задание без звездочки - обязательно к выполнению)

"""

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_worker_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_worker_income(self):
        return self._income_wage + self._income_bonus


pos = Position('Дубинин', 'Виталий', 'инженер газовой отрасли', {'wage': 25000, 'bonus': 17000})
print(pos.get_full_worker_name())
print(pos.get_total_worker_income())
pos = Position('Пластун', 'Дмитрий', 'кадастровый инженер', {'wage': 20000, 'bonus': 15000})
print(pos.get_full_worker_name())
print(pos.get_total_worker_income())
pos = Position('Козлов', 'Михаил', 'механик', {'wage': 10000, 'bonus': 22000})
print(pos.get_full_worker_name())
print(pos.get_total_worker_income())
pos = Position('Воробьёв', 'Алексей', 'дворник', {'wage': 8000, 'bonus': 7000})
print(pos.get_full_worker_name())
print(pos.get_total_worker_income())
pos = Position('Воропаев', 'Сергей', 'стажер-инженер', {'wage': 5000, 'bonus': 9500})
print(pos.get_full_worker_name())
print(pos.get_total_worker_income())
pos = Position('Воронин', 'Макар', 'почтальон', {'wage': 6000, 'bonus': 8000})
print(pos.get_full_worker_name())
print(pos.get_total_worker_income())
