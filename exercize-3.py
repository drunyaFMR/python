# Задание 3


class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return f'Клетки объединилсь в 1 клетку с числом ячеек = {self.cell + other.cell}'

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return f'Появилась новая  клетка с числом ячеек = {self.cell - other.cell}'
        else:
            return f'Не получается! Вторая клетка слишком большая'

    def __mul__(self, other):
        return f'Какая большая клетка! Число ее ячеек = {self.cell * other.cell}'

    def __floordiv__(self, other):
        return f'Теперь это 1 клетка с числом ячеек = {self.cell // other.cell}'

    def make_order(self, number):
        my_str = "\n".join(["\N{Winking Face}" * number for _ in range(self.cell // number)])
        my_str += '\n' + "\N{Winking Face}" * (self.cell % number)
        return my_str


cell_1 = Cell(17)
cell_2 = Cell(9)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(4))
