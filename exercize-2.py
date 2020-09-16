# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна
# принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# Выводит  данные о пользователе как словарь
def my_func(**kwargs):
    return kwargs


print(my_func(name='Ivan', surname='Sidorov', year=1999, city='Moscow', email='IvSid@mail.ru',
              phone_n='+79151514142'))


# Выводит данные о пользователе по элементам
def my_func2(**kwargs):
    for key, value in kwargs.items():
        print(f'{key:<7} - \033[31m{value}\033[0m')


my_func2(name='Ivan', surname='Sidorov', year=1999, city='Moscow', email='IvSid@mail.ru',
         phone_n='+79151514142')
