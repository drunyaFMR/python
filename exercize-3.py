# Задание 3

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        my_str = input('Введите число для списка или "q" для выхода')
        if my_str.isdigit():
            my_list.append(my_str)
        elif my_str == "q":
            print('Goodbye')
            break
        else:
            raise MyError('Вы ввели не число')
    except MyError as err:
        print(err)
    print(f'Cписок - {my_list}')


