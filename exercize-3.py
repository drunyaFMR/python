# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.remove(min(num_1, num_2, num_3))
    return sum(my_list)


a, b, c = input('Enter numbers separated by space').split()
print(my_func(float(a), float(b), float(c)))
