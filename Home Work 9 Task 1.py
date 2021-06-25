"""

Dubinin Vitaliy
Home Work 9 Task 1 (задание без звездочки - обязательно к выполнению)

"""

from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 6))

    def running_traffic_light(self):
        for colors, seconds in cycle(self.__color):
            print(colors, '(wait {} seconds)'.format(seconds))
            sleep(seconds)


traffic_light = TrafficLight()
traffic_light.running_traffic_light()