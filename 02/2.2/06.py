"""
Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов),
когда один объект ссылается на следующий и так по цепочке до последнего.

Для этого объявите в программе два класса:

StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:

obj = StackObj(данные)

Здесь данные - это строка с некоторым содержимым.
Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:

__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:

next - для записи и считывания информации из локального приватного свойства __next;
data - для записи и считывания информации из локального приватного свойства __data.

При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None.
Если проверка не проходит, то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта односвязного списка
В объектах класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;

pop(self) - извлечение последнего объекта с его удалением из односвязного списка;

get_data(self) - получение списка из объектов односвязного списка
(список из строк локального атрибута __data каждого объекта в порядке их добавления, или пустой список,
если объектов нет).

Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


class StackObj:
    def __init__(self, data):
        self.__next = None
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_value):
        if isinstance(new_value, StackObj) or new_value is None:
            self.__next = new_value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_value):
        self.__data = new_value


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj

        if self.top is None:
            self.top = obj

    def pop(self):
        h = self.top
        if self.top is None:
            return

        while h and h.next != self.last:
            h = h.next

        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        res = []
        ptr = self.top

        while ptr:
            res.append(ptr.data)
            ptr = ptr.next

        return res


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']

print(res)
st.pop()
st.pop()
st.pop()
