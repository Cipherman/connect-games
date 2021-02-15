"""Connect Games"""

from players.random_player import random_player
from connect_games._connect_game import State
from connect_games.gomoku import Gomoku
from connect_games.tictactoe import TicTacToe

if __name__ == '__main__':
    play_game = "Gomoku"

    if play_game == "Gomoku":
        game = Gomoku()
    else:
        game = TicTacToe()

    while game.candidate_move:
        (x, y) = random_player(game)
        game.make_move(x, y)

        game.print_board()
        print("Move no. ", game.move_no, " Last move: ", game.game_record[-1])
        print(" ")
        someone_win, side =  game.check_game_result()
        if someone_win:
            print(State.state_string(side), "Win!")
            break
    if not someone_win:
        print("Game Drawn")
