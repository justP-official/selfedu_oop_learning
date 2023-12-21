"""
Подвиг 2. Объявите класс Record (запись), который описывает одну произвольную запись из БД.
Объекты этого класса создаются командой:

r = Record(field_name1=value1,... , field_nameN=valueN)
где field_nameX - наименование поля БД; valueX - значение поля из БД.

В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты по именам полей
(field_name1,... , field_nameN) с соответствующими значениями. Например:

r = Record(pk=1, title='Python ООП', author='Балакирев')
В объекте r появляются атрибуты:

r.pk # 1
r.title # Python ООП
r.author # Балакирев
Также необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError

Если указывается неверный индекс (не целое число или некорректное целое число), то должно генерироваться исключение
командой:

raise IndexError('неверный индекс поля')
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

P.P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта класса Record.
"""


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, item):
        if type(item) == int and -len(self.__dict__) <= item < len(self.__dict__):
            key = list(self.__dict__.keys())[item]
            return self.__dict__[key]
        else:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        if type(key) == int and -len(self.__dict__) <= key < len(self.__dict__):
            setattr(self, tuple(self.__dict__.keys())[key], value)
        else:
            raise IndexError('неверный индекс поля')


r = Record(pk=1, title='Python ООП', author='Балакирев')
r[4] = 'qq'
print(r.__dict__)
