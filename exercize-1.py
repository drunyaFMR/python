# Задание 1
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('text_1.txt', 'w', encoding='utf-8') as my_text:
    while True:
        text_ = input('Enter your text')
        if text_ == '':
            break
        my_text.write(f'{text_}\n')
