class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    # def draw(self):
    #     print("Рисование примитива")


class Line(Geom):
    def draw(self):
        """
        Если базовый класс не содержит метод, то это расширение,
        иначе: переопределение
        """
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        # Geom.__init__(self, x1, y1, x2, y2) -- Bad!
        super().__init__(x1, y1, x2, y2)  # -- Good
        print("Инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)

print(r.__dict__)
