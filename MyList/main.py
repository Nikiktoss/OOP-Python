class NewList:
    def __init__(self, numbers=[]):
        self.new_list = numbers

    def get_list(self):
        return self.new_list

    def __sub__(self, other):
        res = []
        if isinstance(other, NewList):
            sc = other.new_list.copy()
        else:
            sc = other.copy()

        for elem in self.new_list:
            is_exist = False
            for ot in sc:
                if elem == ot and type(elem) == type(ot):
                    is_exist = True
                    del sc[sc.index(ot)]
                    break

            if is_exist is False:
                res.append(elem)

        return NewList(res)

    def __rsub__(self, other):
        res = []
        sc = self.new_list.copy()
        if isinstance(other, NewList):
            prev = other.new_list.copy()
        else:
            prev = other.copy()

        for elem in prev:
            is_exist = False
            for ot in sc:
                if elem == ot and type(elem) == type(ot):
                    is_exist = True
                    del sc[sc.index(ot)]
                    break

            if is_exist is False:
                res.append(elem)

        return NewList(res)

    def __isub__(self, other):
        return self - other


lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
