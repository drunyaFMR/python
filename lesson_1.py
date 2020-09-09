# Задание 1
name = 'Андрей'
age = 29
faculty = 'Data engineering'
print ('Привет' ,name, 'тебе', age, 'лет и ты учишься на факультете:', faculty)
name = input('А как зовут вас?')
age = int(input('Сколько вам лет'))
faculty = input('На каком факультете вы учитесь?')
print(f'Привет {name}! Тебе {age}. Ты учишься на факультете: {faculty}')

# #Задание 2
time = int(input('Введите количество секунд'))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = (time - hours * 3600 - minutes * 60)
print(f'Это будет {hours:02d}:{minutes:02d}:{seconds:02d}')

# Задание 3
n = input("Введите число n")
result = int(n) + int(n + n) + int(n + n + n)
print(f'Сумма {n}+{n+n}+{n+n+n}={result}')

#Задание 4
number = int(input('Введите целое число'))
maxi = 0
while number > 1:
    result: int = number % 10
    if maxi < result:
        maxi = result
    number = number // 10
print(f'Самая большая цифра в этом числе = {maxi}')

# Задание 5
proceeds = int(input('Какова выручка в вашей фирме?'))
costs = int(input('Каковы издержки в вашей фирме?'))
profit = proceeds - costs
if profit > 0:
    print('Ваша фирма приносит прибыль', profit)
    profitability = profit / proceeds
    print(f'Рентабельность вашей выручки = {profitability:.2f}')
elif profit < 0:
    print('Ваша фирма работает в убыток', profit)
else:
    print('Удивительно, но ваша выручка равна вашим издержкам. То есть прибыль равна 0')
personal = int(input('Какое кол-во сотрудников работает у вас в фирме?'))
profit_to_pers = profit / personal
print(f'Прибыль в расчете на 1 сотрудника фирмы = {profit_to_pers:.2f}')

# Задание 6
a = int(input('Сколько километров вы пробежали в первый день?'))
b = int(input('Какого результата вы хотите достичь в километрах?'))
day = 1
while a < b:
    print(f'{day} день: {a:.02f}км')
    a = (a * 0.1) + a
    day += 1
print(f'Если увеличивать нагрузки на 10% желаемого результата вы добьетесь на {day} день пробежав {a:.02f}км')



