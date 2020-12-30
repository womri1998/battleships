from board import Board
from submarine import Submarine


if __name__ == "__main__":
    ships = [Submarine([(0, i) for i in range(5)]), Submarine([(2, 5 + i) for i in range(4)]),
             Submarine([(7, i) for i in range(3)]), Submarine([(i, 8) for i in range(2)]),
             Submarine([(9, i) for i in range(3)])]
    board = Board(ships)
    
