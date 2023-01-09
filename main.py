"""Connect Games"""

from connect_games._connect_game import State
from ConnectGamesEnv import ConnectGamesEnv
from TournamentManager import TournamentManager

from players.random_player import RandomPlayer


if __name__ == '__main__':
    game = "TicTacToe"
    #game = "Gomoku"
    agent = RandomPlayer()
    opponent = RandomPlayer()

    agent_play_black = TournamentManager(game=game, opponent=opponent, agent=agent, agent_side=State.White)

    game_nums = 1000
    agent_play_black.run_tournament(game_nums=game_nums, render=False)  

