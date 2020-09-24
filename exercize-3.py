# Задание 3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as my_text:
    my_dict = {line.split()[0]: line.split()[1] for line in my_text.readlines()}
    numbers = 0
    sum_ = 0
    print('\033[32mСотрудники чей оклад менее 20 тысяч рублей\033[0m')
    for key in my_dict.keys():
        numbers += 1
        sum_ += float(my_dict.get(key))
        if float(my_dict.get(key)) < 20000:
            print(key)
    print(f'\033[34mСредний доход сотрудников = {sum_/numbers:.2f}руб\033[0m')
