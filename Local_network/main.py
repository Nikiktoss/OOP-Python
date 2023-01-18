class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    server_ip = 1

    def __init__(self):
        self.ip = self.server_ip
        self.buffer = []
        self.linked_router = None
        Server.server_ip += 1

    def get_ip(self):
        return self.ip

    def send_data(self, data):
        self.linked_router.buffer.append(data)

    def get_data(self):
        if len(self.buffer) != 0:
            temp = self.buffer.copy()
            self.buffer = []
            return temp
        else:
            return self.buffer


class Router:
    def __init__(self):
        self.buffer = []
        self.linked_servers = []

    def link(self, server):
        self.linked_servers.append(server)
        server.linked_router = self

    def unlink(self, server):
        for i in range(len(self.linked_servers)):
            if self.linked_servers[i].get_ip() == server.get_ip():
                del self.linked_servers[i]
                break

        server.linked_router = None

    def send_data(self):
        for data in self.buffer:
            for server in self.linked_servers:
                if data.ip == server.ip:
                    server.buffer.append(data)

        self.buffer = []


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
print(sv_from.get_data())
print(sv_to.get_data())
