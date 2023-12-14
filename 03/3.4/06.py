"""
Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один
объект ссылается на следующий и так далее).

Давайте снова создадим такую структуру данных. Для этого объявим два класса:

Stack - для управления односвязным списком в целом;
StackObj - для представления отдельных объектов в односвязным списком.

Объекты класса StackObj должны создаваться командой:

obj = StackObj(data)
где data - строка с некоторыми данными.

Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

__data - ссылка на строку с переданными данными;
__next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

Объекты класса Stack создаются командой:

st = Stack()
и каждый из них должен содержать локальный атрибут:

top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

Также в классе Stack следует объявить следующие методы:

push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop_back(self) - удаление последнего объекта из односвязного списка.

Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):

# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj
st += obj

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка
(каждый элемент списка для очередного добавляемого объекта).

P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.

"""


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, (StackObj, type(None))):
            self.__next = value


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj

        if self.top is None:
            self.top = obj

    def pop_back(self):
        h = self.top
        if self.top is None:
            return

        while h and h.next != self.last:
            h = h.next

        if h:
            h.next = None
        self.last = h
        if self.last is None:
            self.top = None

    def __add__(self, other):
        if type(other) == StackObj:
            self.push_back(other)

        return self

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        if type(other) == list:
            for obj in other:
                self.push_back(StackObj(obj))
        return self

    def __imul__(self, other):
        return self * other

