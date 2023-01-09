""" Tournament Manager """
from connect_games._connect_game import State
from ConnectGamesEnv import ConnectGamesEnv

from players.random_player import RandomPlayer

class TournamentManager:

    def __init__(self, game, opponent, agent, agent_side):
        self.game = game
        self.env = ConnectGamesEnv(game=game, opponent=opponent, agent_side=agent_side)
        
        self.agent_side = agent_side
        self.agent = agent

        self.game_collections = {"Won":[], "Lost":[], "Drawn":[]}
        

    def play_games(self, game_nums, render=False):
        games = 0
        observation, info = self.env.reset()
        while True:
            if isinstance(self.agent, RandomPlayer):
                action = self.agent.make_move(self.env.game)
            else:
                action = self.agent.make_move(observation)
            observation, reward, done, info = self.env.step(action)
 
            if render:
                self.env.render_game()

            if done:
                game_record = self.env.export_game_record()
                if reward > 0.0:
                    self.game_collections["Won"].append(game_record)
                elif reward < 0.0:
                    self.game_collections["Lost"].append(game_record)
                else:
                    self.game_collections["Drawn"].append(game_record)

                games+=1 
                if games < game_nums:
                    observation, info = self.env.reset()
                else:
                    break

    def run_tournament(self, game_nums, render=False, save_dir=None):
        self.play_games(game_nums=game_nums, render=render)

        """
        if not save_dir:
            white_path = os.path.join(save_dir, "white_win")
            black_path = os.path.join(save_dir, "black_win")
            draw_path = os.path.join(save_dir, "draw")
            for record in self.win_game_collections:
                with 
        """

        color_name = {State.Black: "Black", State.White: "White"}
        print("Results")
        print(f"total games: {game_nums}")
        print(f"Agent: {color_name[self.agent_side]}")
        print("------------")
        for result, records in self.game_collections.items():
            rate = (len(records) / game_nums) * 100
            print(f"{result} rate: {rate}% ({len(records)} games)")
        print("------------")
