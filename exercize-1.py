# Задание 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(num_1, num_2):
    return num_1 / num_2


while True:
    a = float(input(f'\033[32mEnter first number:\033[0m'))
    b = float(input(f'\033[32mEnter second number:\033[0m'))
    try:
        a / b
    except ZeroDivisionError:
        print('Error! Division by zero!')
    else:
        print(f'\033[31m result = {round(my_func(a, b), 3)}\033[0m')
    end = input('If you want to exit press "Q". If you want continue press "Enter"')
    if end == 'q' or end == 'q'.upper():
        break
    else:
        continue
