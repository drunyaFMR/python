# Задание 1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def my_func():
    try:
        name_file, job_time, rate, prize = argv
    except ValueError:
        return print('You did not specify parameters')
    else:
        try:
            return int(job_time) * float(rate) + float(prize)
        except ValueError:
            return print('You entered incorrect parameters')


if my_func() is not None:
    print(f'Employee salary = {my_func()} руб')
