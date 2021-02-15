"""Connect Games"""

from players.random_player import random_player
from connect_games.connect_game import State
from connect_games.connect_game import ConnectGame

if __name__ == '__main__':
    win_k = 6
    board_x = 6
    board_y = 6

    game = ConnectGame(board_x, board_y, win_k)
    game.turn = State.Black
    while game.candidate_move:
        (x, y) = random_player(game)
        game.move(x, y, game.turn)

        game.print_board()
        game.turn = -game.turn
        print(" ")
        if game.check_move_result(x,y):
            print("Someone Won")
            break