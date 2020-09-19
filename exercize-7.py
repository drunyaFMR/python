# Задание 7
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
# факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial


def fact(num):
    yield factorial(num)


def fact2(num):
    result = 1
    for elem in range(1, num + 1):
        result *= elem
    yield result


while True:
    try:
        number = int(input('Enter integer n = '))
    except ValueError:
        print('\033[31mValueError\033[0m')
    else:
        if number == 0:
            print('0! = 1')
        else:
            # 1 option with module math
            print('\033[32mWith module math\033[0m')
            for n in range(1, number + 1):
                for el in fact(n):
                    print(f'{n}! = {el}')
            # 2 option with own func
            print('\033[32mWith own func\033[0m')
            for n in range(1, number + 1):
                for el in fact2(n):
                    print(f'{n}! = {el}')
        break
