# Задание 2

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abstractmethod
    def payment(self):
        pass

    @property
    def full_payment(self):
        return f'Общая площадь ткани {round((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3), 2)}'


class Coat(Clothes):
    def payment(self):
        return f'Расход ткани для пальто = {round(self.v / 6.5 + 0.5, 2)}'


class Suit(Clothes):
    def payment(self):
        return f'Расход ткани для костюма = {2 * self.h + 0.3}'


coat = Coat(5, 7)
suit = Suit(5, 7)
print(coat.payment())
print(coat.full_payment)
print(suit.payment())
print(suit.full_payment)
