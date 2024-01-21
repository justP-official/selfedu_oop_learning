"""
Посвящение в ООП
Вы прошли серию испытаний и совершили множество подвигов, чтобы лицом к лицу столкнуться с настоящим вызовом, достойным
лишь избранных! Для подтверждения своих знаний и навыков вам предлагается пройти этап посвящения в
объектно-ориентированное программирование. И вот задание, которое выпало на вашу долю.

Руководство компании целыми днями не знает куда себя деть. Поэтому они решили дать задание своим программистам написать
программу игры "Морской бой". Но эта игра будет немного отличаться от классической. Для тех, кто не знаком с этой
древней, как мир, игрой, напомню ее краткое описание.

Каждый игрок у себя на бумаге рисует игровое поле 10 х 10 клеток и расставляет на нем десять кораблей:
однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1.

Корабли расставляются случайным образом, но так, чтобы не выходили за пределы игрового поля и не соприкасались друг с
другом (в том числе и по диагонали).

Затем, игроки по очереди называют клетки, куда производят выстрелы. И отмечают эти выстрелы на другом таком же поле в 10
х 10 клеток, которое представляет поле соперника. Соперник при этом должен честно отвечать: "промах", если ни один
корабль не был задет и "попал", если произошло попадание. Выигрывает тот игрок, который первым поразит все корабли
соперника.

Но это была игра из глубокого прошлого. Теперь же, в компьютерную эру, корабли на игровом поле могут перемещаться в
направлении своей ориентации на одну клетку после каждого хода соперника, если в них не было ни одного попадания.

Итак, лично вам поручается сделать важный фрагмент этой игры - расстановку и управление кораблями в этой игре. А само
задание звучит так.

Техническое задание

В программе необходимо объявить два класса:

Ship - для представления кораблей;
GamePole - для описания игрового поля.

Класс Ship
Класс Ship должен описывать корабли набором следующих параметров:

x, y - координаты начала расположения корабля (целые числа);
length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).
(схема Класс Ship: https://ucarecdn.com/250c5cd8-3534-454f-af88-c58dd60977b4/)

Объекты класса Ship должны создаваться командами:

ship = Ship(length)
ship = Ship(length, tp)
ship = Ship(length, tp, x, y)
По умолчанию (если не указывается) параметр tp = 1, а координаты x, y равны None.

В каждом объекте класса Ship должны формироваться следующие локальные атрибуты:

_x, _y - координаты корабля (целые значения в диапазоне [0; size), где size - размер игрового поля);
_length - длина корабля (число палуб);
_tp - ориентация корабля;
_is_move - возможно ли перемещение корабля (изначально равно True);
_cells - изначально список длиной length, состоящий из единиц (например, при length=3, _cells = [1, 1, 1]).

Список _cells будет сигнализировать о попадании соперником в какую-либо палубу корабля. Если стоит 1, то попадания не 
было, а если стоит значение 2, то произошло попадание в соответствующую палубу.

При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и перемещение корабля по 
игровому полю прекращается.

В самом классе Ship должны быть реализованы следующие методы (конечно, возможны и другие, дополнительные):

set_start_coords(x, y) - установка начальных координат (запись значений в локальные атрибуты _x, _y);
get_start_coords() - получение начальных координат корабля в виде кортежа x, y;

move(go) - перемещение корабля в направлении его ориентации на go клеток 
(go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку); 
движение возможно только если флаг _is_move = True;

is_collide(ship) - проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или 
пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение 
есть и False - в противном случае;

is_out_pole(size) - проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10); 
возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;

С помощью магических методов __getitem__() и __setitem__() обеспечить доступ к коллекции _cells следующим образом:

value = ship[indx] # считывание значения из _cells по индексу indx (индекс отсчитывается от 0)
ship[indx] = value # запись нового значения в коллекцию _cells

Класс GamePole
Следующий класс GamePole должен обеспечивать работу с игровым полем. Объекты этого класса создаются командой:

pole = GamePole(size)
где size - размеры игрового поля (обычно, size = 10).

В каждом объекте этого класса должны формироваться локальные атрибуты:

_size - размер игрового поля (целое положительное число);
_ships - список из кораблей (объектов класса Ship); изначально пустой список.

В самом классе GamePole должны быть реализованы следующие методы (возможны и другие, дополнительные методы):

init() - начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship): 
однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1 
(ориентация этих кораблей должна быть случайной).

Корабли формируются в коллекции _ships следующим образом: 
однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1. 
Ориентация этих кораблей должна быть случайной. Для этого можно воспользоваться функцией randint следующим образом:

[Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), ...]
Начальные координаты x, y не расставленных кораблей равны None.

После этого, выполняется их расстановка на игровом поле со случайными координатами так, чтобы корабли не пересекались 
между собой.

get_ships() - возвращает коллекцию _ships;

move_ships() - перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) в 
направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового 
поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;

show() - отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции _cells каждого 
корабля, вода - значением 0);

get_pole() - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.

Пример отображения игрового поля:

0 0 1 0 1 1 1 0 0 0
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1
0 0 0 0 1 0 1 0 0 1
0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0
0 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0

Пример использования классов (эти строчки в программе не писать):

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()

В программе требуется только объявить классы Ship и GamePole с соответствующим функционалом. На экран выводить ничего не 
нужно.

P.S. Для самых преданных поклонников программирования и ООП. Завершите эту программу, добавив еще один класс SeaBattle 
для управления игровым процессом в целом. Игра должна осуществляться между человеком и компьютером. Выстрелы со стороны
компьютера можно реализовать случайным образом в свободные клетки. Сыграйте в эту игру и выиграйте у компьютера.
"""
from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y

        self._cells = [1 for _ in range(self.length)]

        self.is_move = all(map(lambda x: x == 1, self._cells))

    @property
    def length(self):
        return self._length

    @property
    def tp(self):
        return self._tp

    @property
    def is_move(self):
        return self._is_move

    @is_move.setter
    def is_move(self, value):
        self._is_move = value

    @property
    def cells(self):
        return self._cells

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self.is_move:
            x, y = self.get_start_coords()
            if self.tp == 1:
                self.set_start_coords(x + go, y)
            elif self.tp == 2:
                self.set_start_coords(x, y + go)

    @staticmethod
    def get_coords(ship):
        indexes = (-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1), (0, 0)

        x, y = ship.get_start_coords()

        ship_coords = set()
        full_coords = set()

        if ship.tp == 1:
            ship_coords = {(x + j, y) for j in range(ship.length)}
        elif ship.tp == 2:
            ship_coords = {(x, y + i) for i in range(ship.length)}

        for dx, dy in indexes:
            for x, y in ship_coords:
                full_coords.add((x + dx, y + dy))

        return full_coords, ship_coords

    def is_collide(self, ship):
        self_full_coords, self_coords = self.get_coords(self)
        ship_full_coords, ship_coords = self.get_coords(ship)

        common_coords = self_full_coords & ship_full_coords

        res = (ship_coords & common_coords) | (ship_coords & common_coords)

        return len(res) != 0

    def is_out_pole(self, size):
        x, y = self.get_start_coords()
        if self.tp == 1:
            if x + self.length > size or y > size:
                return True
        elif self.tp == 2:
            if x > size or y + self.length > size:
                return True

        return False

    def take_damage(self, cell_index):
        self[cell_index] = 2
        self.is_move = False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):

        self._cells[key] = value

    def __bool__(self):
        return not all(map(lambda x: x == 2, self.cells))


class GamePole:
    def __init__(self, size):
        self.size = size
        self.pole = [[0 for y in range(self.size)] for x in range(self.size)]

        self._ships = []

        self.init()

    def get_ships(self):
        return self._ships

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)),
                       Ship(3, tp=randint(1, 2)),
                       Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))
                       ]

        self.set_coords()

    def set_coords(self):
        ships = self.get_ships()

        for i in range(len(ships)):
            while True:
                x = randint(0, self.size - 1)
                y = randint(0, self.size - 1)

                tmp_ship = Ship(ships[i].length, ships[i].tp, x, y)

                if i == 0:
                    if not tmp_ship.is_out_pole(self.size):
                        ships[i] = tmp_ship
                        self.add_ship_to_pole(ships[i])
                        break
                    else:
                        continue
                else:
                    if not tmp_ship.is_out_pole(self.size) and \
                            not any(tmp_ship.is_collide(ships[indx]) for indx in range(i) if indx != i):
                        ships[i] = tmp_ship
                        self.add_ship_to_pole(ships[i])
                        break
                    else:
                        continue

    def add_ship_to_pole(self, ship):
        ship_coords = tuple(ship.get_coords(ship)[-1])

        for i in range(ship.length):
            r, c = ship_coords[i]
            self[r, c] = ship[i]

    def update_ships_position(self):
        for i in range(self.size):
            for j in range(self.size):
                self[i, j] = 0

        ships = self.get_ships()

        for ship in ships:
            x, y = ship.get_start_coords()
            length = ship.length

            ship_part = 0

            if ship.tp == 1:
                for j in range(x, x + length):
                    self.pole[y][j] = ship[ship_part]
                    ship_part += 1
            elif ship.tp == 2:
                for i in range(y, y + length):
                    self.pole[i][x] = ship[ship_part]
                    ship_part += 1

    def move_ships(self):
        ships = self.get_ships()

        for i in range(len(ships)):
            if not ships[i].is_move:
                continue

            old_x, old_y = ships[i].get_start_coords()

            ships[i].move(1)
            if not ships[i].is_out_pole(self.size) and \
                    not any(ships[i].is_collide(ships[j]) for j in range(len(ships)) if j != i):
                continue
            else:
                ships[i].set_start_coords(old_x, old_y)
                ships[i].move(-1)
                if ships[i].is_out_pole(self.size) or \
                        any(ships[i].is_collide(ships[j]) for j in range(len(ships)) if j != i):
                    ships[i].set_start_coords(old_x, old_y)

        self.update_ships_position()

    def show(self):
        pole = self.get_pole()

        for row in pole:
            print(*row)

    def get_pole(self):
        return tuple(tuple(row) for row in self.pole)

    def __check_indexes(self, indexes):
        if type(indexes) != tuple or len(indexes) != 2:
            raise IndexError("Неверные координаты")

        if any(not (0 <= x < self.size) for x in indexes if type(indexes) != slice):
            raise IndexError("Неверные координаты")

    def __bool__(self):
        return any(self.get_ships())

    def __getitem__(self, item):
        self.__check_indexes(item)
        x, y = item

        return self.pole[y][x]

    def __setitem__(self, key, value):
        self.__check_indexes(key)
        x, y = key

        self.pole[y][x] = value


class SeaBattle:
    def __init__(self, size):
        self.human_player = GamePole(size)
        self.computer_player = GamePole(size)

        self.step_counter = 0

    def __bool__(self):
        if not self.computer_player:
            return False

        if not self.human_player:
            return False

        return True

    def start_game(self):
        while self:
            if self.step_counter % 2 == 0:
                self.human_move()
            else:
                self.computer_move()

            self.step_counter += 1

        self.check_win()

    def make_shoot(self, pole, x, y):
        ships = pole.get_ships()

        for ship in ships:
            start_ship_x, start_ship_y = ship.get_start_coords()
            end_ship_x, end_ship_y = start_ship_x, start_ship_y

            if ship.tp == 1:
                end_ship_x = start_ship_x + ship.length - 1
            else:
                end_ship_y = start_ship_y + ship.length - 1

            if start_ship_x <= x <= end_ship_x and start_ship_y <= y <= end_ship_y:
                if ship.tp == 1:
                    ship.take_damage(x - start_ship_x)
                else:
                    ship.take_damage(y - start_ship_y)

                if not ship:
                    print("Убит!")

                return

    def computer_move(self):
        while True:
            if not self.human_player:
                break

            self.computer_player.move_ships()
            self.human_player.move_ships()

            print("Ход компьютера")

            self.human_player.show()

            x, y = randint(0, self.human_player.size - 1), randint(0, self.human_player.size - 1)

            if self.human_player[x, y] == 1:
                print("Ранен!")
                self.make_shoot(self.human_player, x, y)

                continue

            elif self.human_player[x, y] == 2:
                print("Эта клетка уже обстреляна! Выбери другую")
                continue

            elif self.human_player[x, y] == 0:
                print("Мимо!")
                break

    def human_move(self):

        while True:
            if not self.computer_player:
                break

            self.computer_player.move_ships()
            self.human_player.move_ships()

            print("Ход человека")
            self.computer_player.update_ships_position()
            self.enemies_locator(self.computer_player.get_pole())

            try:
                x, y = map(lambda x: int(x) - 1, input("Введите координаты x, y через пробел:\n").split())
            except ValueError:
                print("Неверный формат координат. Попробуй ещё раз")
                continue

            try:
                if self.computer_player[x, y] == 1:
                    print("Ранен!")
                    self.make_shoot(self.computer_player, x, y)

                    continue

                elif self.computer_player[x, y] == 2:
                    print("Эта клетка уже обстреляна! Выбери другую")
                    continue

                elif self.computer_player[x, y] == 0:
                    print("Мимо!")
                    break
            except IndexError as e:
                print(e)
                continue

    def check_win(self):
        if not self.computer_player:
            print("Вы победили! :)")
        else:
            print("Вы проиграли! :(")

    def enemies_locator(self, pole):

        for row in pole:
            for cell in row:
                print("X" if cell == 2 else 0, end=' ')
            print()


sb = SeaBattle(10)

sb.start_game()
