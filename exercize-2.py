# Задание 2

class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        a = int(input('Введите число a'))
        b = int(input('Введите число b'))
        if b == 0:
            raise MyOwnError('Делить на 0 нельзя')
    except ValueError:
        print('Вы ввели не число')
        continue
    except MyOwnError as err:
        print(err)
    else:
        print(f'{a} / {b} = {a / b}')
        break
