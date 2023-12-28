"""
Подвиг 8. Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:

air = Aircraft(model, mass, speed, top)
где model - модель самолета (строка); mass - подъемная масса самолета (любое положительное число); speed - максимальная
скорость (любое положительное число); top - максимальная высота полета (любое положительное число).

В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами: _model, _mass, _speed, _top и
соответствующими значениями. Если передаваемые аргументы не соответствуют указанным критериям (строка, любое
положительное число), то генерируется исключение командой:

raise TypeError('неверный тип аргумента')
Далее, в программе объявите следующие дочерние классы:

PassengerAircraft - пассажирский самолет;
WarPlane - военный самолет.

Объекты этих классов создаются командами:

pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число пассажирских мест (целое положительное число)

wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение (словарь); ключи - название оружия,
значение - количество

В каждом объекте классов PassengerAircraft и WarPlane должны формироваться локальные атрибуты с именами _chairs и
_weapons соответственно. Инициализация остальных атрибутов должна выполняться через инициализатор базового класса.

В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых аргументов chairs и weapons.
Если тип данных не совпадает, то генерировать исключение командой:

raise TypeError('неверный тип аргумента')

Создайте в программе четыре объекта самолетов со следующими данными:

PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}

Все эти объекты представить в виде списка planes.

P.S. В программе нужно объявить только классы и сформировать список На экран выводить ничего не нужно.
"""


class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._check_string(model)
        self._check_number(mass)
        self._check_number(speed)
        self._check_number(top)

        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    @staticmethod
    def _check_string(s):
        if type(s) != str:
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def _check_number(x):
        if type(x) != int or not 0 <= x:
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)

        self._check_number(chairs)
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)

        self.__check_dict(weapons)
        self._weapons = weapons

    @staticmethod
    def __check_dict(d):
        if type(d) != dict:
            raise TypeError('неверный тип аргумента')


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
