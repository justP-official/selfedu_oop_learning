"""
Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится задача
создать класс с именем ListInteger с базовым классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных,
генерировать исключение командой:

raise TypeError('можно передавать только целочисленные значения')

Пример использования класса ListInteger (эти строчки в программе не писать):

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.
"""


class ListInteger(list):
    @staticmethod
    def __check_value(value):
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')
        return True

    def __init__(self, items):
        if all(map(self.__check_value, items)):
            super().__init__(items)

    def __setitem__(self, key, value):
        if self.__check_value(value):
            super().__setitem__(key, value)
            
    def append(self, value):
        if self.__check_value(value):
            super().append(value)


s = ListInteger((1, 2))
s[1] = 10
s.append(11)
print(s)
