"""
Подвиг 8. Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой:

r = Rect(x, y, width, height)
где x, y - координаты верхнего левого угла (любые числа); width, height - ширина и высота прямоугольника (положительные
числа). Ось абсцисс (Ox) направлена вправо, ось ординат (Oy) направлена вниз.

В каждом объекте класса Rect должны формироваться локальные атрибуты с именами: _x, _y, _width, _height и
соответствующими значениями. Если переданные аргументы x, y (не числа) и width, height не положительные числа, то
генерировать исключение командой:

raise ValueError('некорректные координаты и параметры прямоугольника')

В классе Rect реализовать метод:

def is_collision(self, rect): ...

который проверяет пересечение текущего прямоугольника с другим (с объектом rect). Если прямоугольники пересекаются, то
должно генерироваться исключение командой:

raise TypeError('прямоугольники пересекаются')

Сформировать в программе несколько объектов класса Rect со следующими значениями:

0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1

Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще один список lst_not_collision, в котором
должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.

P.S. В программе требуется объявить только класс и списки. На экран выводить ничего не нужно.

Подсказка. Для определения пересечения двух прямоугольников, у которых стороны параллельны осям координат
(как в этом подвиге) достаточно проверить, что верхняя грань первого прямоугольника находится ниже нижней грани второго,
или нижняя грань первого прямоугольника выше верхней грани второго. И то же самое для вертикальных граней.
"""


class Rect:
    @staticmethod
    def __check_rect(x, y, width, height):
        if (type(x) not in (int, float) or type(y) not in (int, float)) or (width <= 0 or height <= 0):
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def __init__(self, x, y, width, height):
        self.__check_rect(x, y, width, height)
        self._x = x
        self._y = y
        self._width = width
        self._height = height

        self._x2 = self._x + self._width
        self._y2 = self._y + self._height

    def is_collision(self, rect):
        if not (self._x2 < rect._x or rect._x2 < self._x or self._y2 < rect._y or rect._y2 < self._y):
            raise TypeError('прямоугольники пересекаются')


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except TypeError:
        return True
    return False


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

lst_not_collision = [lst_rect[i] for i in range(len(lst_rect))
                     if not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect)) if i != j)]


print(lst_not_collision)
