# Задание 1

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def get_number(cls, data):
        my_list = []
        char = ''
        for el in data:
            if el.isdigit():
                char += el
            elif char != '':
                my_list.append(char)
                char = ''
        if char != '':
            my_list.append(char)
        return list(map(int, my_list))

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 9999:
                    return f'Data is correct'
                else:
                    return f'Year is incorrect'
            else:
                return f'Month is incorrect'
        else:
            return f'Day is incorrect'


data_1 = Data
print(data_1.get_number('15-22-2017'))
print(data_1.validation(1, 13, 2011))
print(Data.get_number('11 - 11 - 2011'))
print(Data.validation(7, 11, 2022))
print(data_1.get_number('11 - 11 - 2020'))

