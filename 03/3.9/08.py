"""
Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой.

Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)
где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число
объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class StackObj:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.last = None
        self.length = 0

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj

        self.length += 1

    def push_front(self, obj):
        if self.top is None:
            self.last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

        if self.last is None:
            self.last = obj

        self.length += 1

    def __len__(self):
        return self.length

    def __verify_index(self, i):
        if type(i) != int or not 0 <= i < self.length:
            raise IndexError('неверный индекс')

    def __get_by_index(self, indx):
        self.__verify_index(indx)
        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __getitem__(self, item):
        return self.__get_by_index(item).data

    def __setitem__(self, key, value):
        self.__get_by_index(key).data = value

    def __iter__(self):
        h = self.top

        while h:
            yield h
            h = h.next


st = Stack()
st.push_back(StackObj("obj1"))
st.push_back(StackObj("obj2"))
st.push_back(StackObj("obj3"))

st[0] = StackObj("obj4")

print(st[0])

# for s in st:
#     print(s)