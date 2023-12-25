class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # self.draw() -- Error!

    def draw(self):
        print("Рисование примитива")


class Line(Geom):
    name = "Line"

    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    pass
    # def draw(self):
    #     print("Рисование прямоугольника")


g = Geom()
l = Line()
r = Rect()
g.set_coords(0, 0, 0, 0)
l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 2, 2)
print(l.__dict__)
print(r.__dict__)

print(l.name)
print(r.name)

l.draw()
r.draw()
