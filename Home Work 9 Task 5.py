"""

Dubinin Vitaliy
Home Work 9 Task 5 (задание без звездочки - обязательно к выполнению)

"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!!!')


class Pen(Stationery):
    def draw(self):
        print('Ручка рисует!!!')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует!!!')


class Handle(Stationery):
    def draw(self):
        print('Маркер рисует!!!')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()