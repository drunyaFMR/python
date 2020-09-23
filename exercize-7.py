# Задание 7
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
import json

with open('text_7.txt', 'r', encoding='utf-8') as my_text:
    my_dict = {line.split()[0]: float(line.split()[2]) - float(line.split()[3]) for line in my_text.readlines()}
    my_dict1 = {key: value for key, value in my_dict.items() if value > 0}
    my_dict2 = {'average_profit': sum([value for value in my_dict.values() if value > 0])}
    my_dict3 = {key: value for key, value in my_dict.items() if value < 0}
    my_list = [my_dict1, my_dict2, my_dict3]
    [print(el) for el in my_list]
with open('my_file.json', 'w', encoding='utf-8') as write_js:
    json.dump(my_list, write_js, sort_keys=True, indent=4)
