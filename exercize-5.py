# Задание 5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма
# вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func(my_str):
    for num in my_str:
        try:
            new_str.append(float(num))
        except ValueError:
            if num != 'q':
                return False
            else:
                return True
    return new_str


print('\033[32mEnter numbers separated by space. If you want to exit Press "q"\033[0m')
result = []
while True:
    str_ = input('').split()
    new_str = []
    checked = my_func(str_)
    if checked is False:
        print('\033[31mError! Enter only numbers pls\033[0m')
        continue
    elif checked is True:
        print(f'сумма = {sum(new_str) + sum(result)}')
        print('\033[34mGoodbye!\033[0m')
        break
    else:
        print(f'сумма = {sum(new_str) + sum(result)}')
        result.append(sum(new_str))
