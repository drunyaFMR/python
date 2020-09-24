# Задание 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text_5.txt', 'w', encoding='utf-8') as my_text:
    while True:
        numbers = input('Enter numbers separated by spaces').split()
        try:
            new_numbers = list(map(float, numbers))
        except ValueError:
            print('Error! it is not numbers')
            continue
        else:
            break
    my_text.write(' '.join(numbers))
    print(f'Сумма чисел в файле = {sum(new_numbers):.2f}')
