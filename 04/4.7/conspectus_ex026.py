import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt1 = Point(1, 2)

pt2 = Point2D(10, 20)

# pt2.x = 50

# pt2.z = 11 -- Error!

print(pt1.__sizeof__() + pt1.__dict__.__sizeof__())
print(pt2.__sizeof__())

t1 = timeit.timeit(pt1.calc)
t2 = timeit.timeit(pt2.calc)

print(t1, t2)
