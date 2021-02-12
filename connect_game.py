import enum
import numpy as np

class State(enum.IntEnum):
    Empty = 0
    Black = 1
    White = 2

class ConnectGame:

    def __init__(self, x, y, win_k=3):
        self.win_k = win_k
        self.board = np.zeros((x, y))

    def print_board(self):
        for x in range(self.board.shape[0]):
            for y in range(self.board.shape[1]):
                if self.board[x][y] == State.Empty:
                    print("_", end="")
                elif self.board[x][y] == State.Black:
                    print("x", end="")
                elif self.board[x][y] == State.White:
                    print("o",end="")
                else:
                    print(self.board[x][y])
            print("")

    def move(self, x, y, color):
        if self.board[x][y] == State.Empty:
            self.board[x][y] = color
        else:
            print("Point not empty.")
