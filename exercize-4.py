# Задание 4
from random import randint


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} starts ')

    def stop(self):
        print(f'{self.color} {self.name} stops')

    def turn(self):
        turns = ['west', 'southwest', 'northwest', 'east', 'northeast', 'southeast', 'north', 'south']
        print(f'{self.color} {self.name} turns {turns[randint(0, 7)]}')

    def show_speed(self):
        print(f'Current speed = {self.speed} км')


class TownCar(Car):
    def show_speed(self):
        print('You have exceeded the speed limit') if self.speed > 60 else print(f'current speed = {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, max_speed, horse_power):
        super().__init__(speed, color, name, is_police)
        self.characters = {'max_speed': max_speed, 'horse_powers': horse_power}


class WorkCar(Car):
    def show_speed(self):
        print('You have exceeded the speed limit') if self.speed > 40 else print(f'current speed = {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, variety):
        super().__init__(speed, color, name, is_police)
        self.is_police = True
        self.variety = variety


print('\033[32mCar-1 экземпляр класса PoliceCar\033[0m')
car_1 = PoliceCar(55, 'black', 'Toyota', False, 'patrol car')
print(f'Name = {car_1.name}, color = {car_1.color}, speed = {car_1.speed}, isPolice = {car_1.is_police}, '
      f'variety = {car_1.variety}')
car_1.go(), car_1.show_speed(), car_1.turn(), car_1.stop()
print('\033[33mCar-2 экземпляр класса SportCar\033[0m')
car_2 = SportCar(65, 'blue', 'Ferrari', False, '355км', '720л.с')
print(f'Name = {car_2.name}, color = {car_2.color}, speed = {car_2.speed}, isPolice = {car_2.is_police}, characters ='
      f'{car_2.characters}')
print('\033[34mCar-3 экземпляр класса TownCar\033[0m')
car_3 = TownCar(75, 'white', 'Ford', False)
print(f'Name = {car_3.name}, color = {car_3.color}, speed = {car_3.speed}, isPolice = {car_3.is_police}')
car_3.show_speed()
print('\033[35mCar-4 объект класса WorkCar\033[0m')
car_4 = WorkCar(92, 'grey', 'BMW', False)
car_4.go(), car_4.turn(), car_4.stop(), car_4.show_speed()
