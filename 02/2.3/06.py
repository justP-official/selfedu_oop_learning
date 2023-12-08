"""
Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения.
При записи вещественного числа должна выполняться проверка на вещественный тип данных.
Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Присваивать можно только вещественный тип данных.")
Объявите класс Cell, в котором создается объект value дескриптора FloatValue.
А объекты класса Cell должны создаваться командой:

cell = Cell(начальное значение ячейки)
Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:

table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell,
работать с вещественными числами через объект value (начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:

cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3.
Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

P.S. На экран в программе выводить ничего не нужно.
"""


class FloatValue:
    @staticmethod
    def check_value(value):
        if not type(value) == float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)
        

class Cell:
    value = FloatValue()
    
    def __init__(self, value):
        self.value = value
        

class TableSheet:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.cells = [[Cell(float(0.0)) for i in range(self.m)] for j in range(self.n)]


table = TableSheet(5, 3)

val = 1.0

for row in table.cells:
    for cell in row:
        cell.value = val
        val += 1.0
