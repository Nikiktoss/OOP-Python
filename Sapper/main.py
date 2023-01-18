from random import randint


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        if not isinstance(is_mine, bool):
            raise ValueError("недопустимое значение атрибута")

        self.__is_mine = is_mine

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, int) or number < 0 or number > 8:
            raise ValueError("недопустимое значение атрибута")

        self.__number = number

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        if not isinstance(is_open, bool):
            raise ValueError("недопустимое значение атрибута")

        self.__is_open = is_open

    def __bool__(self):
        return self.__is_open is False


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
        self.__pole_cells = self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        result = [[None] * self.M for _ in range(self.N)]

        counter_of_mines = 0
        for i in range(self.N):
            for j in range(self.M):
                choice = randint(0, 1)
                result[i][j] = Cell()
                if choice == 0 and counter_of_mines < self.total_mines:
                    result[i][j].is_mine = True
                    counter_of_mines += 1
                else:
                    result[i][j] = Cell()

        for i in range(self.N):
            for j in range(self.M):
                self.count_mines(result, (i, j))

        return tuple(tuple(result[i]) for i in range(self.N))

    @staticmethod
    def count_mines(matrix, position):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if abs(i - position[0]) == 0 and abs(j - position[1]) == 1 and matrix[i][j].is_mine == True:
                    matrix[position[0]][position[1]].number += 1
                    continue

                if abs(i - position[0]) == 1 and abs(j - position[1]) == 0 and matrix[i][j].is_mine == True:
                    matrix[position[0]][position[1]].number += 1
                    continue

                if abs(i - position[0]) == 1 and abs(j - position[1]) == 1 and matrix[i][j].is_mine == True:
                    matrix[position[0]][position[1]].number += 1
                    continue

    def open_cell(self, i, j):
        if i >= self.N or i < 0 or j >= self.M or j < 0:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

        res = list(list(self.__pole_cells[i]) for i in range(self.N))
        res[i][j].is_open = True
        self.__pole_cells = tuple(tuple(res[i]) for i in range(self.N))


p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
