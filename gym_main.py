"""Connect Games"""

from connect_games._connect_game import State
from ConnectGamesEnv import ConnectGamesEnv

from players.random_player import RandomPlayer

from gymnasium.utils.env_checker import check_env
#from stable_baselines3.common.env_checker import check_env

if __name__ == '__main__':
    game = "TicTacToe"
    #game = "Gomoku"

    agent = RandomPlayer()

    #env = ConnectGamesEnv(game=game, opponent = RandomPlayer(), agent_side = State.White)
    #observation, info = env.reset()
    #print(check_env(env, skip_render_check=True))
    
    #"""
    env = ConnectGamesEnv(game=game, opponent = RandomPlayer(), agent_side = State.Black)
    observation, info = env.reset()
    print(env.game.board)
    

    games = 0
    won = 0
    lost = 0
    drawn = 0 
    for _ in range(10):
        #print(env.game.game_record)
        #print(len(env.game.game_record))
        #print(env.game.candidate_move)
        #print(len(env.game.candidate_move))
        if isinstance(agent, RandomPlayer):
            action = agent.make_move(env.game)
        observation, reward, done, info = env.step(action)
 
        env.render_game()
        print(action)
        print(observation)
        print(info)
        if done:
            games+=1
            if reward > 0.0:
                won+=1
            elif reward < 0.0:
                lost+=1
            else:
                drawn+=1
            if "illegal move" in info["info"]:
                break
            print("game record: ", env.game.game_record)
            print("game record str: ", env.export_game_record())
            observation, info = env.reset()
            

    print(f"Games played = {games}")
    #print(f"Won = {won}, Lost = {lost}, Drawn = {drawn}")
    #print(f"Won = {(won/games)*100}%, Lost = {(lost/games)*100}%, Drawn = {(drawn/games)*100}%")
    #"""       
