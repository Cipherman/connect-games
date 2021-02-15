""" Tic-Tac-Toe """
from connect_games._connect_game import State, Result, ConnectGame


class TicTacToe(ConnectGame):

    def __init__(self):
        ConnectGame.__init__(self, x=3, y=3, win_k=3)
        self.turn = State.Black
        self.move_no = 0
        self.game_record = []

    def make_move(self, x, y):
        ConnectGame.move(self, x=x, y=y, color=self.turn)
        self.turn = -self.turn
        self.move_no += 1
        self.game_record.append((x,y))

    def check_game_result(self):
        x, y = self.game_record[-1] # last move
        return ConnectGame.check_move_result(self, x, y), self.board[x][y]
