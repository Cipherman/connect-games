""" Gomoku (five-in-a-row) """
from connect_games._connect_game import State
from connect_games._connect_game import ConnectGame


class Gomoku(ConnectGame):

    def __init__(self, k=19):
        ConnectGame.__init__(self, x=k, y=k, win_k=5)
        self.turn = State.Black
        self.move_no = 0
        self.game_record = []

    def make_move(self, x, y):
        ConnectGame.move(self, x=x, y=y, color=self.turn)
        self.turn = - self.turn
        self.move_no += 1
        self.game_record.append((x,y))

    def check_game_result(self):
        x, y = self.game_record[-1]
        return ConnectGame.check_move_result(self, x, y), self.board[x][y]
