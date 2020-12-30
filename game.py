from board import Board
from battleship_socket import BattleshipSocket


class Game:
    def __init__(self, board: Board, socket: BattleshipSocket):
        self.board = board
        self.socket = socket

    def my_turn(self):

