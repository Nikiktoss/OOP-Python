from random import randint


SIZE_GAME_POLE = 10


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * self._length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x = self._x + go
            else:
                self._y = self._y + go

    def is_out_pole(self, size):
        if self._tp == 1 and self._x + self._length >= size:
            return True
        elif self._tp == 2 and self._y + self._length >= size:
            return True
        else:
            return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def get_all_coords(self):
        result = []
        if self._tp == 1:
            for i in range(self._length):
                result.append((self._x + i, self._y))
        else:
            for i in range(self._length):
                result.append((self._x, self._y + i))
        return result

    def is_collide(self, ship):
        if ship._x is None and ship._y is None:
            return False

        res_self = self.get_all_coords()
        res_ship = ship.get_all_coords()

        for res_s in res_self:
            for res_sh in res_ship:
                if res_s[0] == res_sh[0] and res_s[1] == res_sh[1]:
                    return True
                elif abs(res_s[0] - res_sh[0]) == 1 and abs(res_s[1] - res_sh[1]) == 1:
                    return True
                elif res_s[0] == res_sh[0] and abs(res_s[1] - res_sh[1]) == 1:
                    return True
                elif abs(res_s[0] - res_sh[0]) == 1 and res_s[1] == res_sh[1]:
                    return True
        return False


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))]

        for i in range(len(self._ships)):
            while True:
                self._ships[i].set_start_coords(randint(0, 9), randint(0, 9))

                if self._ships[i].is_out_pole(self._size) is True:
                    continue

                is_cool = False
                for j in range(len(self._ships)):
                    if i != j:
                        is_cool = self._ships[i].is_collide(self._ships[j])

                        if is_cool is True:
                            break

                if is_cool is False:
                    break

    def get_pole(self):
        result = [[0] * self._size for _ in range(self._size)]

        for ship in self._ships:
            coords = ship.get_all_coords()
            for i in range(ship._length):
                result[coords[i][0]][coords[i][1]] = ship._cells[i]

        return tuple(tuple(result[i]) for i in range(self._size))

    def show(self):
        pole = self.get_pole()
        for p in pole:
            print(*p)

    def get_ships(self):
        return self._ships

    def is_valid_move(self, ship, choice, indx):
        tmp = Ship(ship._length, ship._tp, ship._x, ship._y)
        tmp.move(choice)
        if tmp.is_out_pole(self._size) is True:
            return False

        is_coll = False
        for i in range(len(self._ships)):
            if i != indx:
                is_coll = tmp.is_collide(self._ships[i])
                if is_coll is True:
                    break

        if is_coll is True:
            return False

        return True

    def move_ships(self):
        moves = [-1, 1]
        for i in range(len(self._ships)):
            choice = moves[randint(0, 1)]

            if self.is_valid_move(self._ships[i], choice, i) is True:
                self._ships[i].move(choice)
            elif self.is_valid_move(self._ships[i], choice * (-1), i) is True:
                self._ships[i].move(choice * (-1))


pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
