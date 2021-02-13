"""Connect Games"""

from connect_game import State
from connect_game import ConnectGame

if __name__ == '__main__':
    win_k = 3
    board_x = 3
    board_y = 3

    game = ConnectGame(board_x, board_y, win_k)

    move_x = [1, 3, 2]
    move_y = [1, 2, 1]

    game.print_board()
    for x, y in zip(move_x, move_y):
        print("Move Made")
        game.move(x, y, State.White)
        game.print_board()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
