# Задание 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}')


stationery = Stationery('Title')
stationery.draw()
pencil = Pencil('Карандашом')
pencil.draw()
pen = Pen('Ручкой')
pen.draw()
handle = Handle('Маркером')
handle.draw()
