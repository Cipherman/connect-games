"""Connect Games"""

from players.random_player import RandomPlayer

from connect_games.gomoku import Gomoku
from connect_games.tictactoe import TicTacToe

from game_manager import GameManager

if __name__ == '__main__':
    play = "TicTacToe"

    game_dict = {"Gomoku":Gomoku, "TicTacToe": TicTacToe}
    if play in game_dict:
        game = game_dict[play]
    else:
        print("Game not available!")
        exit()

    manager = GameManager(game)
    manager.play_game(RandomPlayer(), RandomPlayer())


