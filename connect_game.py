import enum
import numpy as np

class State(enum.IntEnum):
    Empty = 0
    Black = 1
    White = 2
    Border = 3


class Result(enum.IntEnum):
    Win = 1
    Lose = -1
    NoResult = 0


class ConnectGame:

    def __init__(self, x, y, win_k=3):
        self.win_k = win_k
        self.turn = State.Black

        # initialize empty board
        self.board = np.zeros((x+2, y+2))
        for i in [0, self.board.shape[0]-1]:
            for j in range(self.board.shape[1]):
                self.board[i][j] = State.Border
        for i in range(self.board.shape[0]):
            for j in [0, self.board.shape[1]-1]:
                self.board[i][j] = State.Border


    def print_board(self):
        for x in range(self.board.shape[0]):
            for y in range(self.board.shape[1]):
                if self.board[x][y] == State.Empty:
                    print("_", end="")
                elif self.board[x][y] == State.Black:
                    print("x", end="")
                elif self.board[x][y] == State.White:
                    print("o",end="")
                elif self.board[x][y] == State.Border:
                    print("B", end="")
                else:
                    print(self.board[x][y])
            print("")


    def move(self, x, y, color):
        if self.board[x][y] == State.Empty:
            self.board[x][y] = color
        else:
            print("Point not empty.")

    def check_move_result(self, x, y):
        color = self.board[x][y]

        # North - South

        # West - East

        # North West - South East

        # North East - South West
