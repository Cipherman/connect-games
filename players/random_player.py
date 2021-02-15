import random

def random_player(game):
    cand_no = random.randint(0, len(game.candidate_move)-1)
    return game.candidate_move[cand_no]