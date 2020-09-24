# Задание 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

try:
    my_text = open('text_1.txt', 'r', encoding='utf-8')
except IOError:
    print('Такого файла нет. Запустите задание 1 где создается этот файл')
else:
    count = 0
    for line in my_text.readlines():
        count += 1
        count_2 = 0
        for words in line.split():
            count_2 += 1
        print(f'В строке {count} - {count_2} слов(а)')
    print(f'Всего строк - {count}')
    my_text.close()
