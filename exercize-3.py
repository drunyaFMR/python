# Задание 3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


pers_1 = Position('Иван', 'Cидоров', 'Механик', 55000, 15000)
print(pers_1.get_full_name())
print(pers_1.get_total_income())
print(pers_1.name, pers_1.surname, pers_1.position, pers_1._income)
