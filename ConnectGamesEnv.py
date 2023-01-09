""" Connect Games Gym Environment """
import numpy as np
import gymnasium as gym
from gymnasium import spaces

from connect_games._connect_game import State

from connect_games.gomoku import Gomoku
from connect_games.tictactoe import TicTacToe


class ConnectGamesEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, game=None, opponent=None, agent_side=None, render_mode=None):

        # connect game structs and stats
        self.game_dict = {"Gomoku": Gomoku, "TicTacToe": TicTacToe}
        self.game_class = game
        self.game = self.game_dict[self.game_class]()

        # connect game settings
        self.board_x = self.game.board.shape[0]
        self.board_y = self.game.board.shape[1]
        self.x = self.game.x
        self.y = self.game.y
        self.win_k = self.game.win_k

        # player settings
        self.agent_side = agent_side
        self.oppo_side = State.White if self.agent_side == State.Black else State.Black
        self._oppo = opponent

        self.observation_space = spaces.Dict(
            {
                "board": spaces.Box(low=0, high=1, shape=(self.board_x * self.board_y, ), dtype=float),
                "turn": spaces.Discrete(5, start=-1),
            }
        )
        self.action_space = spaces.Box(low=0, high=1, shape=(self.board_x * self.board_y, ), dtype=float)

    def _flatten_board(self):
        flat_board =  self.game.board.flatten()
        board_max = flat_board.max()
        board_min = flat_board.min()
        normalized_flat_board = (flat_board - board_min) / (board_max - board_min)

        return normalized_flat_board

    def _get_xy(self, move):
        pos = move.argmax()
        x = pos // self.board_x
        y = pos % self.board_y
        return (x, y)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.game = self.game_dict[self.game_class]()

        if self.oppo_side == State.Black:
            move = self._oppo.make_move(self.game)
            (x, y) = self._get_xy(move)
            self.game.make_move(x,y)

        obs_board = self._flatten_board()
        observation = {"board": obs_board, "turn": self.game.turn}
        info = {"info": "reset"}

        return observation, info

    def step(self, action, render=True):

        done = False
        reward = 0.0
        info = {"info": ""}

        # 2-plys per step
        for _ in range(2):

            move = action if (self.game.turn == self.agent_side) else self._oppo.make_move(self.game)
            (x, y) = self._get_xy(move)

            # illegal move made
            if self.game.board[x][y] != State.Empty:
                done = True
                reward = -1.0 if (self.game.turn == self.agent_side) else 1.0
                info = {"info": f"illegal move ({x},{y})"}
                break

            self.game.make_move(x, y)

            done, side = self.game.check_game_result()
            # player won
            if done:
                reward = 1.0 if (self.game.turn == self.agent_side) else -1.0
                info = {"info": f"{side} won"}
                break

            # game drawn
            if len(self.game.candidate_move) == 0:
                done = True
                reward = 0.0
                info = {"info": "game_drawn"}
                break

        obs_board = self._flatten_board()
        observation = {"board": obs_board, "turn": self.game.turn}

        return observation, reward, done, info

    def render_game(self):
        self.game.print_board()
        print("Move no.", self.game.move_no, " Last move:", self.game.game_record[-1])
        print(" ")

    def export_game_record(self):
        stone_dict = {State.Black: "X", State.White: "O"}
        game_record = []
        num_length = len(str(self.game.board.shape[0] * self.game.board.shape[1])) - 1
        for (x, y) in self.game.game_record:
            game_record.append(
                stone_dict[self.game.board[x][y]]
                + str((len(self.game.board) - 3) * x + y).rjust(num_length, "0")
            )
        return ",".join(game_record)
