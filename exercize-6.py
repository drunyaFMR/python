# Задание 6
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

number = int(input('Введите кол-во наименований товара'))
my_list = []
my_dict = {}
i = 1
while i <= number:
    my_dict['название'] = input(f'Введите название {i} товара')
    my_dict['цена'] = input(f'Введите цену {i} товара')
    my_dict['количество'] = input(f'Введите количество {i} товара')
    my_dict['ед'] = input(f'Введите единицу измерения {i} товара')
    my_tuple = (i, my_dict)
    my_list.append(my_tuple)
    my_dict = {}
    i += 1
print(f'\033[4m\033[31m Готовая структура\033[0m\n {my_list}')
my_list2 = []
my_dict2 = {}
j = 0
while j < number:
    my_list2.append(my_list[j][1].get('название'))
    j += 1
my_dict2['название'] = my_list2
j = 0
my_list2 = []
while j < number:
    my_list2.append(my_list[j][1].get('цена'))
    j += 1
my_dict2['цена'] = my_list2
j = 0
my_list2 = []
while j < number:
    my_list2.append(my_list[j][1].get('количество'))
    j += 1
my_dict2['количество'] = my_list2
j = 0
my_list2 = []
while j < number:
    my_list2.append(my_list[j][1].get('ед'))
    j += 1
my_dict2['ед'] = my_list2
print(f'\033[4m\033[31m Аналитика данных\033[0m\n {my_dict2}')
