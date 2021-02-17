""" Game play manager """
from connect_games._connect_game import State

class GameManager:

    def __init__(self, game):
        self._game_class = game
        self._game = None

    def play_game(self, black_player, white_player):
        self._game = self._game_class()
        self._game_record = []

        while self._game.candidate_move:
            if self._game.turn == State.Black:
                (x, y) = black_player.make_move(self._game)
            else:
                (x, y) = white_player.make_move(self._game)

            self._game.make_move(x,y)
            self.render_game()
            someone_win, side = self._game.check_game_result()
            if someone_win:
                print(State.state_string(side), "Win!")
                break
        if not someone_win:
            print("Game Drawn!")

    def render_game(self):
        self._game.print_board()
        print("Move no.", self._game.move_no, " Last move:", self._game.game_record[-1])
        print(" ")

    def export_game_record(self):
        stone_dict = {State.Black: "X", State.White: "O"}
        game_record = []
        num_length = len(str(self._game.board.shape[0] * self._game.board.shape[1]))
        print(num_length)
        for (x, y) in self._game.game_record:
            game_record.append(stone_dict[self._game.board[x][y]] +
                               str((len(self._game.board) - 3) * x + y).rjust(num_length, '0'))
        print(','.join(game_record))

