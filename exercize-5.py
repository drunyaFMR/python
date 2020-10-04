# Задание 5

class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


a = complex(1, 2)
b = complex(3, 4)
print(f'Исходные числа a = {a} и b = {b}')
number_1 = ComplexNumber(a)
number_2 = ComplexNumber(b)
print(f'Cумма чисел = {number_1 + number_2}')
print(f'Произведение чисел = {number_1 * number_2}')
