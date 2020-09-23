# Задание 6
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.

with open('text_6.txt', 'r', encoding='utf-8') as my_text:
    my_dict = {line.split()[0]: line.split()[1:] for line in my_text.readlines()}
    my_list = []
    new_list = []
    for el in my_dict.values():
        if len(my_list) != 0:
            new_list.append(my_list)
            my_list = []
        for elem in el:
            num = ''
            for char in elem:
                if char.isdigit():
                    num += char
                elif num != '':
                    my_list.append(int(num))
                    num = ''
    new_list.append(my_list)
    sum_list = [sum(new_list[i]) for i in range(0, len(new_list))]
    i = 0
    for key in my_dict.keys():
        new_dict = {key: sum_list[i]}
        my_dict.update(new_dict)
        i += 1
    print(my_dict)
