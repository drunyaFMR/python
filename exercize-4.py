# Задание 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

from googletrans import Translator

translator = Translator()
with open('text_4.txt', 'r', encoding='utf-8') as my_text:
    my_line = []
    for line in my_text.readlines():
        for el in line.split():
            if el == line.split()[0]:
                result = translator.translate(line.split()[0], src='en', dest='ru')
                my_line.append(result.text)
            else:
                my_line.append(el)
with open('text_4_2.txt', 'w', encoding='utf-8') as my_text2:
    new_line = [my_line[i:i + 3] for i in range(0, len(my_line), 3)]
    for line in new_line:
        my_text2.write(' '.join(line) + '\n')
print('Check file text_4_2.txt')
