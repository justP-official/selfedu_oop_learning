"""
Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных.

Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией.
Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу);
индекс отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx
(в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
P.S. На экран в программе ничего выводить не нужно.
"""


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __get_by_indx(self, indx):
        counter = 0
        ptr = self.head
        while ptr and counter < indx:
            counter += 1
            ptr = ptr.next

        return ptr

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def remove_obj(self, indx):
        ptr = self.__get_by_indx(indx)

        if ptr is None:
            return

        left = ptr.prev
        right = ptr.next

        if left:
            left.next = right
        if right:
            right.prev = left

        if self.head == ptr:
            self.head = right
        if self.tail == ptr:
            self.tail = left

    def __len__(self):
        if self.head is None:
            return 0

        ptr = self.head
        counter = 0
        while ptr:
            counter += 1
            if ptr.next:
                ptr = ptr.next
        return counter

    def __call__(self, indx, *args, **kwargs):
        ptr = self.__get_by_indx(indx)

        return ptr.data if ptr else None
