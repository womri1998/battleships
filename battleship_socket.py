from random import randint
import socket


PORT = 5555
MAX_MESSAGE_SIZE = 4096
NO_SESSION = ''
HOST_SERVER = ''
HOST_CLIENT = '127.0.0.1'
START_SESSION = "000"
ACCEPT = "001"
DECLINE = "002"
KEEP_SESSION = "003"
ATTACK = "004"
ERROR = "005"
DISCONNECT = "006"
READY = "007"
DROWNED = "008"
KEEP_ALIVE = "009"


class BattleshipSocket:
    def __init__(self, my_socket: socket.socket):
        self.server_socket = my_socket
        self.connection = my_socket
        self.address = HOST_SERVER
        self.session = NO_SESSION

    def listen(self):
        self.server_socket.bind((HOST_SERVER, PORT))
        self.server_socket.listen(1)
        self.receive_session()

    def receive_session(self):
        self.connection, self.address = self.server_socket.accept()
        data = self.connection.recv(MAX_MESSAGE_SIZE).decode()
        code, session, version = data[:3], data[3:7], data[7:]
        if (code == START_SESSION and session == NO_SESSION) \
                or code == KEEP_SESSION and session == self.session:
            self.accept(session)
            return True
        else:
            self.decline()
            return False

    def generate_session_number(self):
        self.session = hex(randint(0, 16 ** 4 - 1))[2:]
        self.pad_session_number()

    def pad_session_number(self):
        self.session = '0' * (4 - len(self.session)) + self.session

    def start_session(self):
        self.generate_session_number()
        self.server_socket.connect((HOST_CLIENT, PORT))
        self.server_socket.send((START_SESSION + self.session).encode())

    def accept(self, session_number):
        self.session = session_number
        self.connection.send(ACCEPT.encode())

    def decline(self):
        self.connection.send(DECLINE.encode())
        self.connection = self.server_socket
        self.address = HOST_SERVER
        self.session = NO_SESSION

    def keep_session(self):
        self.server_socket.connect((HOST_CLIENT, PORT))
        self.server_socket.send((KEEP_SESSION + self.session).encode())
        data = self.server_socket.recv(MAX_MESSAGE_SIZE).decode()
        if data == ACCEPT:
            return True
        else:  # data == DECLINE
            return False

    def attack(self, x, y):
        self.connection.send((ATTACK + str(x) + str(y)).encode())

    def enemy_attack(self):
        data = self.connection.recv(MAX_MESSAGE_SIZE).decode()
        code, x, y = data[:3], int(data[3:4]), int(data[4:])
        return x, y

    def ready(self):
        self.server_socket.send(READY.encode())

    def keep_alive(self):
        self.connection.send(KEEP_ALIVE.encode())
