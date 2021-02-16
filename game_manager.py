""" Game play manager """
from connect_games._connect_game import State

class GameManager:

    def __init__(self, game):
        self._game_class = game

    def play_game(self, black_player, white_player):
        game = self._game_class()

        while game.candidate_move:
            if game.turn == State.Black:
                (x, y) = black_player.make_move(game)
            else:
                (x, y) = white_player.make_move(game)

            game.make_move(x,y)
            self.render_game(game)
            someone_win, side = game.check_game_result()
            if someone_win:
                print(State.state_string(side), "Win!")
                break
        if not someone_win:
            print("Game Drawn!")

    def render_game(self, game):
        game.print_board()
        print("Move no.", game.move_no, " Last move:", game.game_record[-1])
        print(" ")

