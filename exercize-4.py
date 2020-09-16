# Задание 1
# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
# выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.

# С помощью **
def my_func(num_1, num_2):
    return num_1 ** num_2


# С помощью цикла
def my_func2(num_1, num_2):
    result = 1
    for i in range(0, num_2, -1):
        result = num_1 * result
    return 1 / result


while True:
    try:
        x = float(input('Enter a positive real number x = '))
    except ValueError:
        print('Error! x in not a number')
        continue
    if x <= 0:
        print('Error! x <= 0')
        continue
    else:
        while True:
            try:
                y = int(input('Enter a negative integer y = '))
            except ValueError:
                print('Error! y is not an integer.')
                continue
            if y >= 0:
                print('Error! y >= 0')
                continue
            else:
                break
    print(f'{x}^({y}) = {round(my_func(x, y), 8)}')
    print(f'{x}^({y}) = {round(my_func2(x, y), 8)}')
    break
