# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# через list
season = ['зима', 'весна', 'лето', 'осень']
answers = [(1, 2, 12), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
answer = int(input('Введите месяц в виде целого числа'))
i = 0
while i < len(answers):
    if answer in answers[i]:
        print(f'Это {season[i]}')
        break
    else:
        i += 1

# через dict
season_dict = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
answer = int(input('Введите месяц в виде целого числа'))
for key in season_dict:
    if answer in season_dict.get(key):
        print(f'Это {key}')
        break
    else:
        continue
