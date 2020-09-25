# Задание 1
from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for i in range(3):
            print(f'\033[5m\033[31m{TrafficLight.__color[0]}\033[0m')
            sleep(7)
            print(f'\033[33m{TrafficLight.__color[1]}\033[0m')
            sleep(2)
            print(f'\033[32m{TrafficLight.__color[2]}\033[0m')
            sleep(5)


a = TrafficLight()
a.running()
