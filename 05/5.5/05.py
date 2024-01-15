"""
Подвиг 5. Объявите класс Box (ящик), объекты которого создаются командой:

box = Box(name, max_weight)
где name - название ящика (строка); max_weight - максимальный суммарный вес вещей в ящике (любое положительное число).

В каждом объекте этого класса должны формироваться локальные атрибуты:

_name - ссылка на параметр name;
_max_weight - ссылка на параметр max_weight;
_things - список из вещей, хранящиеся в ящике (изначально пустой список).

В классе Box объявите метод:

def add_thing(self, obj)

для добавления новой вещи в ящик, где obj - кортеж из двух значений:

(название_вещи, вес_вещи)

Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится больше величины _max_weight, то
генерировать исключение командой:

raise ValueError('превышен суммарный вес вещей')

Затем, объявите еще один класс BoxDefender, который должен работать совместно с менеджером контекста следующим образом
(эти строчки в программе не писать):

box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))
    ...
Здесь b - это ссылка на объект класса Box. Если при добавлении вещей возникает исключение ValueError, то объект box
должен оставаться без изменений (с теми вещами, что были до вызова менеджера контекста). Иначе, все добавленные вещи
остаются в объекте box.

P.S. В программе только объявить классы. Выводить что-либо на экран и использовать классы не нужно.
"""


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._current_weight = 0
        self._things = []

    def add_thing(self, obj):
        w = obj[1]

        if self._current_weight + w > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        else:
            self._things.append(obj)
            self._current_weight += w


class BoxDefender:
    def __init__(self, box):
        self.__box = box
        self.__tmp = self.__box._things[:]

    def __enter__(self):
        return self.__box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.__box._things[:] = self.__tmp
        return False