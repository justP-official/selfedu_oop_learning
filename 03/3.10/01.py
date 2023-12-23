"""
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом.
Объекты этого класса будут создаваться командой:

game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:

pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:

cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:

value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

Также с объектами класса Cell должна выполняться функция:

bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:

res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать
исключение командой:

raise IndexError('некорректно указанные индексы')

Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны
быть три публичных атрибута (атрибуты класса):

FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)
В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

Также в классе TicTacToe должны быть следующие объекты-свойства (property):

is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:

bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном
случае.

Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):

game = TicTacToe()
game.init()

Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть в
"Крестики-нолики" между человеком и компьютером.

P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.

P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.
"""

import random


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    @staticmethod
    def __check_indexes(indx):
        if type(indx) != tuple or len(indx) != 2:
            raise IndexError('неверный индекс клетки')
        if any(not (0 <= x < 3) for x in indx if type(x) != slice):
            raise IndexError('неверный индекс клетки')

    @staticmethod
    def __check_cell(cell):
        if not cell:
            raise ValueError('клетка уже занята')

    @classmethod
    def true_x(cls, x):
        return x.value == cls.HUMAN_X

    @classmethod
    def true_o(cls, o):
        return o.value == cls.COMPUTER_O

    def __init__(self):
        self.pole = tuple(tuple(Cell() for y in range(3)) for x in range(3))
        self.step_counter = 0

    def __getitem__(self, item):
        self.__check_indexes(item)
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(3))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(3))

        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_indexes(key)
        r, c = key
        self.__check_cell(self.pole[r][c])

        if not self.is_human_win and not self.is_computer_win and not self.is_draw:
            self.pole[r][c].value = value

    def init(self):
        self.step_counter = 0

        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL

    def show(self):
        tokens = ('_', 'X', '0')

        for row in self.pole:
            for cell in row:
                print(tokens[cell.value], end=' ')
            print()

    def human_go(self):
        if not self:
            return
        while True:
            item = tuple(map(int, input().split()))

            try:
                self[item] = self.HUMAN_X
            except IndexError:
                continue
            except ValueError:
                continue

            break

        self.step_counter += 1

    def computer_go(self):
        if not self:
            return
        while True:
            item = (random.randint(0, 2), random.randint(0, 2))

            try:
                self[item] = self.COMPUTER_O
            except ValueError:
                continue

            break

        self.step_counter += 1

    @property
    def is_human_win(self):
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                return True

        for i in range(3):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                return True

        if all(self.pole[i][i].value == self.HUMAN_X for i in range(3)) or all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(3)):
            return True

        return Fals

    @property
    def is_computer_win(self):
        for row in self.pole:
            if all(x.value == self.COMPUTER_O for x in row):
                return True

        for i in range(3):
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                return True

        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(3)) or all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(3)):
            return True

        return False

    @property
    def is_draw(self):
        return all(x.value != self.FREE_CELL for row in self.pole for x in row)

    def __bool__(self):
        if self.is_human_win:
            return False
        if self.is_computer_win:
            return False
        if self.is_draw:
            return False
        return True


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

