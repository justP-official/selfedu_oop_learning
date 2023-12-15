class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24

        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Правый операнд должен быть int или Clock")

        return other if isinstance(other, int) else other.seconds

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds - sc)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds -= sc
        return self

    def __mul__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds * sc)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds *= sc
        return self

    def __truediv__(self, other):
        if not isinstance(other, (float, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds / sc)

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds /= sc
        return self

    def __floordiv__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds // sc)

    def __rfloordiv__(self, other):
        return self // other

    def __ifloordiv__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds //= sc
        return self

    def __mod__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds % sc)

    def __rmod__(self, other):
        return self % other

    def __imod__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds %= sc
        return self

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __ne__(self, other):
        sc = self.__verify_data(other)
        return self.seconds != sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.seconds >= sc


c1 = Clock(1000)
c2 = Clock(2000)

print(100 < c2)
