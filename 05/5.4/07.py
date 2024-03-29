"""
Значимый подвиг 7. Вам поручается разработать класс TupleData, элементами которого могут являются только объекты
классов: CellInteger, CellFloat и CellString.

Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString, объекты которых создаются командами:

cell_1 = CellInteger(min_value, max_value)
cell_2 = CellFloat(min_value, max_value)
cell_3 = CellString(min_length, max_length)
где min_value, max_value - минимальное и максимальное допустимое значение в ячейке; min_length, max_length - минимальная
и максимальная допустимая длина строки в ячейке.

В каждом объекте этих классов должны формироваться локальные атрибуты с именами _min_value, _max_value или _min_length,
_max_length и соответствующими значениями.

Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (property) с именем:

value - для записи и считывания значения в ячейке (изначально возвращает значение None).

Если в момент записи новое значение не соответствует диапазону [min_value; max_value] или [min_length; max_length],
то генерируется исключения командами:

raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
Все три класса исключений должны быть унаследованы от одного общего класса:

CellException

Далее, объявите класс TupleData, объекты которого создаются командой:

ld = TupleData(cell_1, ..., cell_N)
где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).

Обращение к отдельной ячейке должно выполняться с помощью оператора:

value = ld[index] # считывание значения из ячейке с индексом index
ld[index] = value # запись нового значения в ячейку с индексом index

Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом. Если значение index выходит за диапазон
[0; число ячеек-1], то генерировать исключение IndexError.

Также с объектами класса TupleData должны выполняться следующие функции и операторы:

res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)
Все эти классы в программе можно использовать следующим образом:

ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран отображать ничего не нужно.
"""


class CellException(Exception):
    def __init__(self, *args):
        self.error_text = args[0] if args else ''

    def __str__(self):
        return self.error_text


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    EXCEPTION = CellException()

    def check_value(self, value):
        if not self._min_value <= value <= self._max_value:
            raise self.EXCEPTION

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.check_value(value)
        self._value = value


class CellInteger(Cell):
    EXCEPTION = CellIntegerException('значение выходит за допустимый диапазон')


class CellFloat(Cell):
    EXCEPTION = CellFloatException('значение выходит за допустимый диапазон')


class CellString(Cell):
    EXCEPTION = CellStringException('длина строки выходит за допустимый диапазон')

    def __init__(self, min_length, max_length):
        super().__init__(min_length, max_length)
        self._min_length = min_length
        self._max_length = max_length

    def check_value(self, value):
        if not self._min_length <= len(value) <= self._max_length:
            raise self.EXCEPTION


class TupleData:
    def __init__(self, *args):
        self.data = args

    def __getitem__(self, item):
        return self.data[item].value

    def __setitem__(self, key, value):
        self.data[key].value = value

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for i in range(len(self.data)):
            yield self.data[i].value
