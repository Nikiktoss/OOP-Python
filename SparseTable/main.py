class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.data = {}
        self.__row_index = list()
        self.__col_index = list()

    def __count_rows_cols(self, col, row):
        if col + 1 > self.cols:
            self.cols = col + 1

        if row + 1 > self.rows:
            self.rows = row + 1

    def add_data(self, row, col, data):
        self.data[(row, col)] = data
        self.__col_index.append(col)
        self.__row_index.append(row)
        self.__count_rows_cols(col, row)

    def remove_data(self, row, col):
        if (row, col) not in self.data:
            raise IndexError('ячейка с указанными индексами не существует')
        else:
            del self.data[(row, col)]
            del self.__row_index[self.__row_index.index(row)]
            del self.__col_index[self.__col_index.index(col)]

            if row + 1 == self.rows and row not in self.__row_index:
                self.rows = max(self.__row_index) + 1

            if col + 1 == self.cols and col not in self.__col_index:
                self.cols = max(self.__col_index) + 1

    def __getitem__(self, item):
        if item not in self.data:
            raise ValueError('данные по указанным индексам отсутствуют')
        else:
            return self.data[item].value

    def __setitem__(self, key, value):
        if key not in self.data:
            self.add_data(key[0], key[1], Cell(value))
        else:
            self.data[key].value = value


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
