"""
Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')

В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. Иначе, v
должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Vector:
    def __init__(self, *args):
        self.coords = args

    def get_coords(self):
        return self.coords

    def check_length(self, other):
        if len(self.get_coords()) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self.check_length(other)
        return Vector(*(self.get_coords()[i] + other.get_coords()[i] for i in range(len(self.get_coords()))))

    def __sub__(self, other):
        self.check_length(other)
        return Vector(*(self.get_coords()[i] - other.get_coords()[i] for i in range(len(self.get_coords()))))


class VectorInt(Vector):
    @staticmethod
    def __check_args(*args):
        if any(map(lambda x: type(x) != int, args)):
            raise ValueError('координаты должны быть целыми числами')

    def __init__(self, *args):
        self.__check_args(*args)
        super().__init__(*args)

    def __add__(self, other):
        try:
            self.__check_args(*other.get_coords())
            self.check_length(other)
            return VectorInt(*(self.get_coords()[i] + other.get_coords()[i] for i in range(len(self.get_coords()))))
        except ValueError:
            self.check_length(other)
            return Vector(*(self.get_coords()[i] + other.get_coords()[i] for i in range(len(self.get_coords()))))

    def __sub__(self, other):
        try:
            self.__check_args(*other.get_coords())
            self.check_length(other)
            return VectorInt(*(self.get_coords()[i] - other.get_coords()[i] for i in range(len(self.get_coords()))))
        except ValueError:
            self.check_length(other)
            return Vector(*(self.get_coords()[i] - other.get_coords()[i] for i in range(len(self.get_coords()))))


v1 = Vector(1, 2, 3, 4)
v2 = Vector(1, 1, 1, 1)
# res = v1 - v2
# print(res.get_coords())

vi1 = VectorInt(1, 2)
vi2 = Vector(1, 1.1)
res = vi1 + vi2
print(res.get_coords())
