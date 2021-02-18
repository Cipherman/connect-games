import random


class RandomPlayer:
    def __init__(self):
        self.name = "Random Player"

    def make_move(self, game):
        cand_no = random.randint(0, len(game.candidate_move)-1)
        return game.candidate_move[cand_no]
