"""
Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме.

Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

cell = Cell(data)
где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с
соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str и
т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()

При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с атрибутом type_data объекта
класса TableValues), должно генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')

При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят за
диапазон размера таблицы, то генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for y in range(self.cols)] for x in range(self.rows)]

    def __check_indexes(self, indexes):
        x, y = indexes
        if (type(x) != int and type(y) != int) or (self.rows <= x < 0 or self.cols <= y < 0):
            raise IndexError('неверный индекс')

    def __check_value(self, value):
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, item):
        self.__check_indexes(item)
        row, col = item
        return self.table[row][col].data

    def __setitem__(self, key, value):
        self.__check_indexes(key)
        row, col = key
        self.__check_value(value)
        self.table[row][col].data = value

    def __iter__(self):
        for row in self.table:
            yield (x.data for x in row)


table = TableValues(2, 3)
table[0, 0] = 10
for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
