# Задание 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
print('Исходный список', my_list)
while True:
    number = int(input('Введите новый элемент рейтинга в виде натурального числа'))
    if number in my_list:
        reiteration = my_list.count(number)
        ind = my_list.index(number)
        my_list.insert(ind + reiteration, number)
    else:
        i = 0
        for el in my_list:
            if number < my_list[i]:
                i += 1
                if i == len(my_list):
                    my_list.append(number)
                    break
            else:
                my_list.insert(i, number)
                break
    print(my_list)
    yes = input('Хотите добавить еще один элемент?(да/нет)')
    if yes.lower() == 'да':
        continue
    else:
        print('Пока')
        break
