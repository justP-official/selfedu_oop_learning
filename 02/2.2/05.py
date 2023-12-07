"""
Подвиг 5. Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:

wnd = WindowDlg(заголовок окна, ширина, высота)
В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:

__title - заголовок окна (строка);
__width, __height - ширина и высота окна (числа).

В классе WindowDlg необходимо реализовать метод:

show() - для отображения окна на экране (выводит в консоль строку в формате: "<Заголовок>: <ширина>, <высота>",
например "Диалог 1: 100, 50").

Также в классе WindowDlg необходимо реализовать два объекта-свойства:

width - для изменения и считывания ширины окна;
height - для изменения и считывания высоты окна.

При изменении размеров окна необходимо выполнять проверку:

- переданное значение является целым числом в диапазоне [0; 10000].

Если хотя бы один размер изменился (высота или ширина),
то следует выполнить автоматическую перерисовку окна (вызвать метод show()).
При начальной инициализации размеров width, height вызывать метод show() не нужно.
"""


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @staticmethod
    def check_value(x):
        return isinstance(x, int) and 0 <= x <= 10000

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_value):
        if self.check_value(new_value):
            self.__width = new_value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_value):
        if self.check_value(new_value):
            self.__height = new_value
            self.show()