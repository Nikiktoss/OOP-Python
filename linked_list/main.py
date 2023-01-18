class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __call__(self, indx):
        counter = 0
        tmp = self.head

        while counter < indx:
            tmp = tmp.next
            counter += 1

        return tmp.data

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        if indx < 0 or indx >= len(self):
            raise IndexError("Элемента с данным индексом не существует!")

        if indx == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
        else:
            counter = 0
            tmp = self.head

            while counter < indx:
                tmp = tmp.next
                counter += 1

            tmp.prev.next = tmp.next
            if tmp.next is not None:
                tmp.next.prev = tmp.prev
            else:
                self.tail = tmp.prev

    def __len__(self):
        counter = 0
        tmp = self.head

        while tmp is not None:
            tmp = tmp.next
            counter += 1

        return counter


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))

print(len(linked_lst))
print(linked_lst(1))
