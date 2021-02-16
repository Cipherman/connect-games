import enum
import numpy as np


class State(enum.IntEnum):
    Empty = 0
    Black = 1
    White = -1
    Border = 3

    @classmethod
    def state_string(cls, state):
        if state == cls.Empty:
            return "Empty"
        if state == cls.Black:
            return "Black"
        if state == cls.White:
            return "White"
        if state == cls.Border:
            return "Border"


class Result(enum.IntEnum):
    Win = 1
    NoResult = 2
    Draw = 3

    @classmethod
    def result_string(cls, result):
        if result == cls.Win.value:
            return "Win"
        if result == cls.Draw.value:
            return "Draw"
        if result == cls.NoResult.value:
            return "No Result"



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

        self.candidate_move = []
        for x in range(self.board.shape[0]):
            for y in range(self.board.shape[1]):
                if self.board[x][y] == State.Empty:
                    self.candidate_move.append((x,y))

    def print_board(self):
        for x in range(self.board.shape[0]):
            for y in range(self.board.shape[1]):
                if self.board[x][y] == State.Empty:
                    print("_", end="")
                elif self.board[x][y] == State.Black:
                    print("x", end="")
                elif self.board[x][y] == State.White:
                    print("o", end="")
                elif self.board[x][y] == State.Border:
                    print("B", end="")
                else:
                    print(self.board[x][y])
            print("")

    def move(self, x, y, color):
        if self.board[x][y] == State.Empty:
            self.board[x][y] = color
            self.candidate_move.remove((x,y))
        else:
            print("Point not empty.")

    def check_board_result(self):
        for x in range(self.board.shape[0]):
            for y in range(self.board.shape[1]):
                if self.check_move_result(x, y):
                    return True, self.board[x][y]
        return False, None

    def check_move_result(self, x, y):
        # North - South
        if self._check_direction_state(x, y, [1, 0]):
            return True
        # West - East
        if self._check_direction_state(x, y, [0, 1]):
            return True
        # North West - South East
        if self._check_direction_state(x, y, [1, -1]):
            return True
        # North East - South West
        if self._check_direction_state(x, y, [1, 1]):
            return True
        return False

    def _check_direction_state(self, x, y, step):
        count = 1
        _x = x
        _y = y
        color = self.board[x][y]
        for i in range(self.win_k):
            _x += step[0]
            _y += step[1]
            if self._check_position_state(_x, _y, color):
                count += 1
            else:
                break
        _x = x
        _y = y
        for i in range(self.win_k):
            _x -= step[0]
            _y -= step[1]
            if self._check_position_state(_x, _y, color):
                count += 1
            else:
                break
        return count >= self.win_k

    def _check_position_state(self, x, y, color):
        if self.board[x][y] == color:
            return True
        else:
            return False
