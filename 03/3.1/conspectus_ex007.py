class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # @classmethod
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Access denied")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # print("__setattr__")
        if key == "z":
            raise AttributeError("Invalid attribute name")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        # print("__getattr__ " + item)
        return False

    def __delattr__(self, item):
        print("__delattr__ " + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)

pt2 = Point(10, 20)

# pt1.set_bound(-100)

print(pt1.__dict__)
#
# a = pt1.y
#
# print(a)

# pt1.z = 5 -- Error

print(pt1.q)
