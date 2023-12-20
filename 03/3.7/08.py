"""
Большой подвиг 8. Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым
полем. Будем полагать, что оно имеет размеры N x M клеток.
Каждая клетка будет представлена объектом класса Cell и содержать либо число мин вокруг этой клетки, либо саму мину.

Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем.
Объект этого класса должен формироваться командой:

pole = GamePole(N, M, total_mines)
И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole
(используйте паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__()).

Объект pole должен иметь локальный приватный атрибут:

__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов),
состоящий из объектов класса Cell.

Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):

pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

Далее, в самом классе GamePole объявите следующие методы:

init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение
атрибута __is_open объекта Cell в ячейке (i, j) на True;
show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).

Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint модуля
random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин).
Область охвата - соседние (прилегающие) клетки (8 штук).

В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то
генерируется исключение командой:

raise IndexError('некорректные индексы i, j клетки игрового поля')
Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:

cell = Cell()
При этом в самом объекте создаются следующие локальные приватные свойства:

__is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
__number - число мин вокруг клетки (целое число от 0 до 8);
__is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:

is_mine - для записи и чтения информации из атрибута __is_mine;
number - для записи и чтения информации из атрибута __number;
is_open - для записи и чтения информации из атрибута __is_open.

В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False,
либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:

raise ValueError("недопустимое значение атрибута")
С объектами класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка закрыта и False - если открыта.

Пример использования классов (эти строчки в программе писать не нужно):

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
P.S. В программе на экран выводить ничего не нужно, только объявить классы.
"""
from random import randint


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for i in range(self.M)) for j in range(self.N))
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def __check_coords(self, x, y):
        if (type(x) != int or not 0 <= x <= self.N) or (type(y) != int or not 0 <= y <= self.M):
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def init_pole(self):
        for row in self.pole:
            for cell in row:
                cell.is_open = False
                cell.is_mine = False

        counter = 0
        while counter < self.total_mines:
            x = randint(0, self.N-1)
            y = randint(0, self.M-1)
            if self.pole[x][y].is_mine:
                continue
            self.pole[x][y].is_mine = True
            counter += 1

        self.count_mines()

    def count_mines(self):
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

        for x in range(self.N):
            for y in range(self.M):
                if not self.pole[x][y].is_mine:
                    mines = sum(
                        (self.pole[x + i][y + j].is_mine for i, j in indx if 0 <= x + i < self.N and 0 <= y + j < self.M))
                    self.pole[x][y].number = mines

    def open_cell(self, i, j):
        self.__check_coords(i, j)
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            for cell in row:
                print(f"{cell.number}" if cell.is_open else "#", end=' ')
            print()


class Cell:
    def __init__(self, is_mine=False, number=0, is_open=False):
        self.__is_mine = is_mine
        self.__number = number
        self.__is_open = is_open

    def __bool__(self):
        return False if self.is_open else True

    @staticmethod
    def is_bool(x):
        if type(x) != bool:
            raise ValueError("недопустимое значение атрибута")

    @staticmethod
    def is_number(x):
        if type(x) != int or not 0 <= x <= 8:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        self.is_bool(value)
        self.__is_mine = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        self.is_bool(value)
        self.__is_open = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.is_number(value)
        self.__number = value


pole = GamePole(10, 20, 10)
pole.show_pole()

pole.open_cell(2, 4)
pole.show_pole()
