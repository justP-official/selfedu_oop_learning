"""
Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:

pt = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа).
При этом в объектах класса Point должны формироваться следующие локальные свойства:

__x, __y - координаты точки на плоскости.

и один геттер:

get_coords() - возвращение кортежа текущих координат __x, __y

Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:

r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или

r2 = Rectangle(x1, y1, x2, y2)

Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний.

При этом, в объектах класса Rectangle (вне зависимости от способа их создания)
должны формироваться следующие локальные свойства:

__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).

Также к классе Rectangle должны быть реализованы следующие методы:

set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;

get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника
(ссылки на локальные свойства __sp и __ep);

draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)".
Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).
"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, a, b, c=None, d=None):
        self.__sp = self.__ep = None

        if isinstance(a, Point) and isinstance(b, Point):
            self.__sp = a
            self.__ep = b
        elif all(map(lambda x: type(x) in (int, float), (a, b, c, d))):
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    # def __init__(self, *args):
    #     if len(args) == 4:
    #         self.__sp = Point(args[0], args[1])
    #         self.__ep = Point(args[2], args[3])
    #     else:
    #         self.__sp = args[0]
    #         self.__ep = args[1]

    def set_coords(self, sp: Point, ep: Point):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        tmp = self.get_coords()
        print(f"Прямоугольник с координатами: {tmp[0].get_coords()} {tmp[1].get_coords()}")


rect = Rectangle(1, 2, 3, 4)
# sp, ep = rect.get_coords()
# print(type(sp))
# a, b = sp.get_coords()
# c, d = ep.get_coords()
# print(a == 1, b == 2, c == 3, d == 4)
# print(rect.get_coords()[1])
rect.draw()

rect2 = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = rect2.get_coords()
print(rect2.get_coords())
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"
print(a == 1, b == 2, c == 3, d == 4)
rect2.draw()
