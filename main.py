"""Connect Games"""

from connect_game import State
from connect_game import ConnectGame

if __name__ == '__main__':
    win_k = 3
    board_x = 3
    board_y = 3

    game = ConnectGame(board_x, board_y, win_k)

    move_x = [1, 3, 2, 3, 1, 3]
    move_y = [1, 2, 1, 1, 3, 3]
    turn = [State.White, State.Black, State.White, State.Black, State.White, State.Black]

    game.print_board()
    print("")
    for x, y, turn in zip(move_x, move_y, turn):
        print("Move Made: ", x, y)
        game.move(x, y, turn)
        game.print_board()
        print(game.check_move_result(x,y))
        print(" ")
