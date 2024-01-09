class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.__length = (x * x + y * y) ** 0.5

    # @property
    # def length(self):
    #     return self.__length
    #
    # @length.setter
    # def length(self, value):
    #     self.__length = value


class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


pt = Point2D(1, 2)

pt3 = Point3D(10, 20, 30)
pt3.z = 30
# print(pt3.__dict__)

# print(pt.length)
