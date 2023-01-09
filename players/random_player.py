import random
import numpy as np

class RandomPlayer:
    def __init__(self):
        self.name = "Random Player"

    def make_move(self, game):
        cand_no = random.randint(0, len(game.candidate_move)-1)
        (x, y) = game.candidate_move[cand_no]
        action = np.zeros((game.board.shape[0], game.board.shape[1]))
        action[x][y] = 1
        return np.ravel(action)
