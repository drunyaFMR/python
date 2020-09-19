# Задание 5
# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
# произведения всех элементов списка.

from itertools import accumulate
from functools import reduce
import operator


my_list = [el for el in range(100, 1001) if el % 2 == 0]
# 1 вариант
print(max(list(accumulate(my_list, operator.mul))))


# 2 вариант через reduce
def my_func(prev_el, el):
    return prev_el * el


print((reduce(my_func, my_list)))
