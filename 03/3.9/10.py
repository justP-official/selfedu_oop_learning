"""
Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами.
Объекты этого класса должны создаваться командой:

m1 = Matrix(rows, cols, fill_value)
где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы
(должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

Также объекты можно создавать командой:

m2 = Matrix(list2D)
где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных).
Если список list2D не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')

Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')

Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы),
то генерировать исключение:

raise IndexError('недопустимые значения индексов')

Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1

Во всех этих операция должна формироваться новая матрица с соответствующими значениями.
Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')

Пример для понимания использования индексов (эти строчки в программе писать не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""


class Matrix:
    @staticmethod
    def __check_args(args):
        rows, cols, fill_value = args
        if any(map(lambda x: type(x) != int, (rows, cols))) or type(fill_value) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    @staticmethod
    def __check_lst(lst):
        rows = len(lst)
        cols = len(lst[0])

        if not all(len(r) == cols for r in lst):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

        for i in range(rows):
            for j in range(cols):
                if type(lst[i][j]) not in (int, float):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __check_indexes(self, indexes):
        x, y = indexes
        if not 0 <= x < self.rows or not 0 <= y < self.cols:
            raise IndexError('недопустимые значения индексов')

    @staticmethod
    def __check_value(value):
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')

    def __check_sizes(self, matrix):
        m_rows = matrix.rows
        m_cols = matrix.cols

        if m_rows != self.rows or m_cols != self.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __init__(self, *args):
        if len(args) == 3:
            self.__check_args(args)
            self.rows, self.cols, self.fill_value = args
            self.lst2D = [[self.fill_value for y in range(self.cols)] for x in range(self.rows)]
        else:
            self.__check_lst(*args)
            self.lst2D = list(*args)
            self.rows = len(self.lst2D)
            self.cols = len(self.lst2D[0])

    def __getitem__(self, item):
        self.__check_indexes(item)
        row, col = item
        return self.lst2D[row][col]

    def __setitem__(self, key, value):
        self.__check_indexes(key)
        self.__check_value(value)

        row, col = key

        self.lst2D[row][col] = value

    def __add__(self, other):
        new_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        if isinstance(other, Matrix):
            self.__check_sizes(other)

            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix[i][j] = self.lst2D[i][j] + other.lst2D[i][j]

        elif isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix[i][j] = self.lst2D[i][j] + other

        return Matrix(new_matrix)

    def __sub__(self, other):
        new_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        if isinstance(other, Matrix):
            self.__check_sizes(other)

            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix[i][j] = self.lst2D[i][j] - other.lst2D[i][j]

        elif isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix[i][j] = self.lst2D[i][j] - other

        return Matrix(new_matrix)


mt = Matrix([[1, 2], [3, 4]])
mt2 = Matrix([[1, 2], [3, 4]])
res = mt + mt2
print(res.lst2D)
# res = mt[0, 0] # 1
# res = mt[0, 1] # 2
# res = mt[1, 0] # 3
# res = mt[1, 1]