# Задание 2

class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def result(self):
        cover = 25
        thickness = 5
        return (self._length * self._width * cover * thickness) / 1000


a = Road(20, 5000)
print(f'Масса асфальта необходимая для покрытия {a.result()} т')
