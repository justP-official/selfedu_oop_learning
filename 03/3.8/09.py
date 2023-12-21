"""
Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)
где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение).
В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе,
генерируется исключение:

raise ValueError('превышен суммарный вес предметов')
Также с объектами класса Bag должны выполняться следующие команды:

t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del bag[indx] # удаление вещи из сумки, расположенной по индексу indx
Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

raise IndexError('неверный индекс')
Пример использования классов (эти строчки в программе не писать):

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Thing:
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.current_weight = 0
        self.things = []

    def __check_weight(self, thing: Thing, current_weight):
        if thing.weight + current_weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def __check_index(self, indx):
        if type(indx) != int or not 0 <= indx < len(self.things):
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        self.__check_weight(thing, self.current_weight)
        self.things.append(thing)
        self.current_weight += thing.weight

    def __getitem__(self, item):
        self.__check_index(item)
        return self.things[item]

    def __delitem__(self, key):
        self.__check_index(key)
        self.current_weight -= self.things[key].weight
        del self.things[key]

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__check_weight(value, self.current_weight - self.things[key].weight)
        self.current_weight -= self.things[key].weight
        self.things[key] = value
        self.current_weight += value.weight


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))


b[1] = Thing('рубашка', 600)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
