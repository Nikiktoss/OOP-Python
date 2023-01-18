import math


class Vertex:
    _id = 0

    def __init__(self):
        self._links = []
        self._id = Vertex._id
        Vertex._id += 1

    @property
    def links(self):
        return self._links

    def add(self, link):
        if link not in self._links:
            self._links.append(link)


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, dist):
        self._dist = dist

    def __eq__(self, other):
        if self._v1 == other._v1 and self._v2 == other._v2:
            return True

        if self._v1 == other._v2 and self._v2 == other._v1:
            return True

        return False


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        is_exist = False
        for vertex in self._vertex:
            if v._id == vertex._id:
                is_exist = True
                break

        if is_exist is False:
            self._vertex.append(v)

    def add_link(self, link):
        is_exist = False
        for l in self._links:
            if l == link:
                is_exist = True
                break

        if is_exist is False:
            self._links.append(link)
            link._v1.add(link)
            link._v2.add(link)
            self.add_vertex(link._v1)
            self.add_vertex(link._v2)

    def create_matrix(self):
        max = 0
        for v in self._vertex:
            if v._id > max:
                max = v._id

        matrix = [[math.inf for _ in range(max + 1)] for _ in range(max + 1)]

        for vertex in self._vertex:
            for link in vertex._links:
                matrix[link.v1._id][link.v2._id] = link.dist
                matrix[link.v2._id][link.v1._id] = link.dist

        for i in range(len(self._vertex)):
            matrix[i][i] = 0

        return matrix

    def find_path(self, start_v, stop_v):
        matr = self.create_matrix()
        P = [[v for v in range(len(matr))] for u in range(len(matr))]

        for k in range(len(matr)):
            for i in range(len(matr)):
                for j in range(len(matr)):
                    d = matr[i][k] + matr[k][j]
                    if matr[i][j] > d:
                        matr[i][j] = d
                        P[i][j] = k

        u = stop_v._id
        path = [u]
        while u != start_v._id:
            u = P[u][start_v._id]
            path.append(u)

        return (self.get_vertex(path[::-1]), self.get_links(path[::-1]))

    def get_vertex(self, path):
        vertex = []
        for elem in path:
            for v in self._vertex:
                if elem == v._id:
                    vertex.append(v)
                    break

        return vertex

    def get_links(self, path):
        links = []
        for i in range(1, len(path)):
            for link in self._links:
                if path[i - 1] == link._v1._id and path[i] == link._v2._id:
                    links.append(link)
                    break

                if path[i - 1] == link._v2._id and path[i] == link._v1._id:
                    links.append(link)
                    break

        return links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self.dist = dist


map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()

map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

map2.add_link(Link(v2, v1))
assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"

map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)

assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"
