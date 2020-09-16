# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу
# должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, # но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

def int_func(str_):
    for word in str_:
        for el in word:
            if ord(el) in range(97, 123):
                continue
            else:
                return False
    return (' '.join(str_)).title()


while True:
    my_str = input('Enter words').split()
    checked = int_func(my_str)
    if checked is False:
        print('Error! Enter words only with small latin letters')
    else:
        print(checked)
        break
