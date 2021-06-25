"""

Dubinin Vitaliy
Home Work 9 Task 4 (задание без звездочки - обязательно к выполнению)

"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехал!!!'.format(self.name))

    def stop(self):
        print('{} остановился!'.format(self.name))

    def turn(self, direction):
        print('{} поворачивает {}!'.format(self.name, direction))

    def show_speed(self):
        print('Текущая скорость Вашего автомобиля:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Осторожно!!! Скорость Вашего автомобиля превышена!!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Текущая скорость Вашего автомобиля:', self.speed)
        if self.speed > 40:
            print('Осторожно!!! Скорость Вашего автомобиля превышена!!!')


class PoliceCar(Car):
    pass


sport_car = SportCar(340, 'Малиновый цвет', 'Спорткар', False)
town_car = TownCar(115, 'Цвет металлик серебристый', 'Городской автомобиль', False)
work_car = WorkCar(70, 'Цвет желто-черный', 'Рабочая автомашина', False)
police_car = PoliceCar(180, 'Бело-голубой цвет', 'Полицейский автомобиль', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('налево!!')
police_car.turn('налево!!')
work_car.turn('направо!!')
town_car.turn('направо!!')
