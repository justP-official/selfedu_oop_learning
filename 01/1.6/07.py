"""
Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов.
Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
"""


class SingletonFive:
    counter = 0
    __instanse = None

    def __new__(cls, *args, **kwargs):
        if cls.counter < 5:
            cls.counter += 1
            cls.__instanse = super().__new__(cls)

        return cls.__instanse

    def __init__(self, name):
        self.name = name



objs = [SingletonFive(str(n)) for n in range(10)]

print(id(objs[4]), id(objs[5]), id(objs[6]),)
print(objs[0].counter)
