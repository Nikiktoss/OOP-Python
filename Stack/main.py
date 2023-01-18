class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            tmp = self.top
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = obj

    def pop_back(self):
        if self.top.next is None:
            self.top = None
        else:
            prev = self.top
            tmp = self.top
            while tmp.next is not None:
                prev = tmp
                tmp = tmp.next
            del tmp
            prev.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        for elem in other:
            self.push_back(StackObj(elem))
        return self

    def __imul__(self, other):
        return self * other


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
