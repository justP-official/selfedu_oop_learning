class Geom:
    pass


class Line(Geom):
    pass


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


g = Geom()
l = Line()

print(issubclass(Line, Geom))  # True
print(issubclass(Geom, Line))  # False
print(isinstance(l, Line))  # True

v = Vector([1, 2, 3])

print(v)
