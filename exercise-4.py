from abc import ABC, abstractmethod


class Stock:
    def __init__(self, title, num, number):
        self.title = title
        self.num = num
        self.number = number
        self.reception_list, self.transfer_list, self.transfer_list_2 = [], [], []
        self.count_p, self.count_s, self.count_x = 0, 0, 0
        self.my_dict_p, self.my_dict_s, self.my_dict_x, self.transfer_dict = {}, {}, {}, {}

    def reception(self):
        try:
            self.title = input('Введите наименование товара(Принтер, cканер или ксерокс)')
            self.num = int(input('Введите кол-во данного товара(в виде целого числа)'))
            if self.num < 0:
                return print('Кол-во товара не может быть меньше 0')
        except ValueError:
            return print('Вы ввели не число')
        if self.title.lower() == 'принтер':
            printer.full_reception()
            self.my_dict_p = {self.title: self.num + self.count_p}
            self.count_p += self.num
        elif self.title.lower() == 'сканер':
            scanner.full_reception()
            self.my_dict_s = {self.title: self.num + self.count_s}
            self.count_s += self.num
        elif self.title.lower() == 'ксерокс':
            xerox.full_reception()
            self.my_dict_x = {self.title: self.num + self.count_x}
            self.count_x += self.num
        else:
            print('Ошибка ввода наименования товара')
        self.reception_list = [self.my_dict_p, self.my_dict_s, self.my_dict_x]

    def get_info_stock(self):
        if len(self.reception_list) == 0:
            return print('На данный момент на складе пусто')
        else:
            return print(f'На данный момент на складе - {self.reception_list}')

    def transfer(self):
        f = input('В какую фирму отправляем технику?')
        try:
            self.title = input('Выберите какую технику отправляем(Принтер, сканер или ксерокс)')
            self.number = int(input('Какое кол-во техники отправляем'))
            if self.number < 0:
                return print('Кол-во товара не может быть меньше 0')
        except ValueError:
            return print('Вы ввели не число')
        if self.title.lower() == 'принтер':
            self.my_dict_p, printer.list_p = stock.transfer_1(self.my_dict_p, self.title, self.number, f, printer.list_p)
        elif self.title.lower() == 'сканер':
            self.my_dict_s, scanner.list_s = stock.transfer_1(self.my_dict_s, self.title, self.number, f, scanner.list_s)
        elif self.title.lower() == 'ксерокс':
            self.my_dict_x, xerox.list_x = stock.transfer_1(self.my_dict_x, self.title, self.number, f, xerox.list_x)
        else:
            print('Ошибка ввода наименования')
        self.reception_list = [self.my_dict_p, self.my_dict_s, self.my_dict_x]


    @staticmethod
    def transfer_1(dict_, title, number, firm, list_):
        if dict_.get(title) is not None and dict_.get(title) - number >= 0:
            dict_ = {title: dict_.get(title) - number}
            print('Выберите какие модели будем отправлять')
            [print(f'{ind} - {el}') for ind, el in enumerate(list_, 1)]
            temp = input('Введите номера нужных моделей через пробел -->> ').split()
            temp = [el - 1 for el in list(map(int, temp))]
            for el in temp:
                stock.transfer_list.append(list_[el])
            stock.transfer_dict = {firm: stock.transfer_list}
            stock.transfer_list = []
            stock.transfer_list_2.append(stock.transfer_dict)
            list_ = [i for j, i in enumerate(list_) if j not in temp]
            return dict_, list_
        else:
            return print('На складе не достаточно данного товара')

    @staticmethod
    def get_transfer_info():
        print('------------------Все переданые товары-------------------')
        return [print(el) for el in stock.transfer_list_2]



class OfficeEquipment(ABC):
    def __init__(self, color, price, brand, name):
        self.color = color
        self.price = price
        self.brand = brand
        self.name = name

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def full_reception(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, color, price, brand, name, category):
        super().__init__(color, price, brand, name)
        self.category = category
        self.name = 'Принтер'
        self.dict_p = {}
        self.list_p = []

    def get_info(self):
        if len(self.list_p) == 0:
            return print('На данный момент на складе нет принтеров')
        else:
            return print(f'Информация о всех имеющихся принтерах - {printer.list_p}')

    def full_reception(self):
        for i in range(1, stock.num + 1):
            self.color = input(f'Введите цвет {i} принтера')
            self.price = input(f'Введите цену {i} принтера')
            self.brand = input(f'Введите фирму {i} принтера')
            self.category = input(f'Введите категорию {i} принтера(лазерный, струйный, 3D)')
            self.dict_p = {self.name: [self.color, self.price, self.brand, self.category]}
            self.list_p.append(self.dict_p)


class Scanner(OfficeEquipment):
    def __init__(self, color, price, brand, kind, name):
        super().__init__(color, price, brand, name)
        self.name = 'Cканер'
        self.dict_s = {}
        self.list_s = []
        self.kind = kind

    def get_info(self):
        if len(self.list_s) == 0:
            return print('На данный момент на складе нет сканеров')
        else:
            return print(f'Информация о всех имеющихся сканерах - {scanner.list_s}')

    def full_reception(self):
        for i in range(1, stock.num + 1):
            self.color = input(f'Введите цвет {i} сканера')
            self.price = input(f'Введите цену {i} сканера')
            self.brand = input(f'Введите фирму {i} сканера')
            self.kind = input(f'Введите разновидность {i} сканера(планшетный, протяжной, ручной)')
            self.dict_s = {self.name: [self.color, self.price, self.brand, self.kind]}
            self.list_s.append(self.dict_s)


class Xerox(OfficeEquipment):
    def __init__(self, name, color, price, brand, print_speed):
        super().__init__(name, color, price, brand)
        self.name = 'Ксерокс'
        self.print_speed = print_speed
        self.dict_x = {}
        self.list_x = []

    def get_info(self):
        if len(self.list_x) == 0:
            return print('На данный момент на складе нет ксероксов')
        else:
            return print(f'Информация о всех имеющихся ксероксах - {xerox.list_x}')

    def full_reception(self):
        for i in range(1, stock.num + 1):
            self.color = input(f'Введите цвет {i} ксерокса')
            self.price = input(f'Введите цену {i} ксерокса')
            self.brand = input(f'Введите фирму {i} ксерокса')
            self.print_speed = input(f'Введите скорость печати(стр/мин) {i} ксерокса(10, 10-20, 20-30, >30)')
            self.dict_x = {self.name: [self.color, self.price, self.brand, f'{self.print_speed} cтр/мин']}
            self.list_x.append(self.dict_x)


def menu():
    while True:
        print('===================================================')
        print('                    СКЛАД                          ')
        print('===================================================')
        print(' 1 - Информация о товаре на складе')
        print(' 2   Подробная информация о каждом товаре')
        print(' 3 - Прием товара')
        print(' 4 - Передача товара')
        print(' 5 - Информация о передаче товара')
        print(' 0 - Выход')
        print('===================================================')
        response = input('Введите нужное число -> ')
        if response == '1':
            stock.get_info_stock()
        elif response == '2':
            menu_2()
        elif response == '3':
            stock.reception()
        elif response == '4':
            stock.transfer()
        elif response == '5':
            stock.get_transfer_info()
        elif response == '0':
            print('Пока')
            break
        else:
            print('Некорректный ввод')


def menu_2():
    while True:
        print('---------------------------------')
        print(' 1 - Информация о принтерах')
        print(' 2 - Информация о сканнерах')
        print(' 3 - Информаци о ксероксах')
        print(' 0 - Выход в главное меню')
        print('---------------------------------')
        x = input('Введите нужное число ->  ')
        if x == '1':
            printer.get_info()
        elif x == '2':
            scanner.get_info()
        elif x == '3':
            xerox.get_info()
        elif x == '0':
            break
        else:
            print('Некорректный ввод')


stock = Stock('', '', '')
printer = Printer('', '', '', '', '')
scanner = Scanner('', '', '', '', '')
xerox = Xerox('', '', '', '', '')
menu()
