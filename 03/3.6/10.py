"""
Подвиг 10 (на повторение). Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие
дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). Иначе,
генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")
Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны выполняться
условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")
Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)),
где p - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle.
"""


class Side:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = Side()
    b = Side()
    c = Side()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = a + b + c

    def __len__(self):
        return int(self.p)

    def __call__(self):
        p = self.p / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def __setattr__(self, key, value):
        if (key == 'a' and not self.check_triangle(value, self.b, self.c)) or \
                (key == 'b' and not self.check_triangle(self.a, value, self.c)) or \
                (key == 'c' and not self.check_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)

    @staticmethod
    def check_triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True
