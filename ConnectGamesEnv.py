""" Game play manager """
from connect_games._connect_game import State

import gymnasium as gym
from gymnasium import spaces

class ConnectGamesEnv(gym.Env):
    metadata = {"render_modes":["human"]}

    def __init__(self, game=None, agent=None, opponent=None, agent_sidem, render_mode=None):

        # connect game structs and stats
        self._game_class = game
        self._game = self._game_class()
        self.win_game_collections = {State.Black: [], State.White: []}
        self.drawn_game_collections = []        

        # connect game settings
        self.x = self._game.x
        self.y = self._game.y
        self.win_k = self._game.win_k

        # player settings
        self.agent_side = agent
        self.oppo_side = State.White if self.agent_side == State.Black else State.Black
        self.oppo = opponent

        self.observation_space = spaces.Box(low=-1, high=3, shape=(self.x, self.y), dtype=np.int)
        self.action_space = spaces.Box(low=0, high=max(self.x, self.y), shape=(2, 1), dtype=np.int)

    def reset(self):
        self._game = self._game_class()
        self._game_record = []
 
        observation = {"game": self._game, "record": self._game_record}
        info = {"status": "reset"}
         
        return observation, info

    #def step(self, black_player, white_player, render=True):
    def step(self, move, render=True):

        (x, y) = self.oppo.make_move(self._game)
        self._game.make_move(x,y)

        done, side = self._game.check_game_result()
        if done:
            self.win_game_collections[side].append(self.export_game_record())
        if self._game.move_no == (self.x * self.y) # board is full
            self.drawn_game_collections.append(self.export_game_record())

    def render_game(self):
        self._game.print_board()
        print("Move no.", self._game.move_no, " Last move:", self._game.game_record[-1])
        print(" ")

    def export_game_record(self):
        stone_dict = {State.Black: "X", State.White: "O"}
        game_record = []
        num_length = len(str(self._game.board.shape[0] * self._game.board.shape[1]))-1
        for (x, y) in self._game.game_record:
            game_record.append(stone_dict[self._game.board[x][y]] +
                               str((len(self._game.board) - 3) * x + y).rjust(num_length, '0'))
        return ','.join(game_record)

