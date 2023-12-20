"""
Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными)
координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться
исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
P.S. В программе на экран выводить ничего не нужно, только объявить класс.
"""


class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __validate(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        self.__validate(other)
        tmp = [a + b for a, b in zip(self.coords, other.coords)]
        return Vector(*tmp)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.__validate(other)
            self.coords = [a + b for a, b in zip(self.coords, other.coords)]
        else:
            self.coords = [a + other for a in self.coords]
        return self

    def __sub__(self, other):
        self.__validate(other)
        tmp = [a - b for a, b in zip(self.coords, other.coords)]
        return Vector(*tmp)

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.__validate(other)
            self.coords = [a - b for a, b in zip(self.coords, other.coords)]
        else:
            self.coords = [a - other for a in self.coords]
        return self

    def __mul__(self, other):
        self.__validate(other)
        tmp = [a * b for a, b in zip(self.coords, other.coords)]
        return Vector(*tmp)

    def __eq__(self, other):
        try:
            self.__validate(other)
        except ArithmeticError:
            return False
        for i in range(len((self.coords))):
            if self.coords[i] != other.coords[i]:
                return False
        return True

