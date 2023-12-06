class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coords must be a numbers")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)

# print(pt.__x, pt.__y) -- Error

pt.set_coord(10, 20)

print(pt.get_coord())
