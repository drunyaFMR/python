# Задание 1

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix])

    def __add__(self, other):
        result = []
        if len(self.matrix[0]) != len(other.matrix[1]) or len(self.matrix) != len(other.matrix):
            return f'Операция сложения матриц определена только для матриц одинакового размера.'
        else:
            for el in zip(self.matrix, other.matrix):
                my_list = []
                for numbers in zip(el[0], el[1]):
                    my_list.append(sum(numbers))
                result.append(my_list)
            return '\n'.join(['\t'.join([str(j) for j in i]) for i in result])


a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
b = Matrix([[8, 7, 6, 5], [4, 3, 2, 1]])
print('Матрица a =')
print(a)
print('Матрица b = ')
print(b)
print('Матрица с(сумма матриц a и b) = ')
print(a + b)
