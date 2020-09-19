# Задание 6
#  Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
# должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count
from itertools import cycle

print('With break')
# 1 вариант с break
my_list = []
new_list = []
for i in count(5):
    if i > 7:
        break
    else:
        my_list.append(i)
print(my_list)
j = 0
for i in cycle(my_list):
    if j > 5:
        break
    new_list.append(i)
    j += 1
print(new_list)

print('Without break')
# 2 вариант без break
my_list = []
new_list = []
iter_ = count(5)
for i in range(3):
    my_list.append(next(iter_))
print(my_list)
iter_ = cycle(my_list)
for i in range(6):
    new_list.append(next(iter_))
print(new_list)
