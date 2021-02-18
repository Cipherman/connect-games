""" Game play manager """
from connect_games._connect_game import State

class GameManager:

    def __init__(self, game):
        self._game_class = game
        self._game = None
        self.win_game_collections = {State.Black: [], State.White: []}
        self.drawn_game_collections = []

    def play_game(self, black_player, white_player, render=True):
        self._game = self._game_class()
        self._game_record = []

        while self._game.candidate_move:
            if self._game.turn == State.Black:
                (x, y) = black_player.make_move(self._game)
            else:
                (x, y) = white_player.make_move(self._game)

            self._game.make_move(x,y)
            if render:
                self.render_game()
            someone_win, side = self._game.check_game_result()
            if someone_win:
                if render:
                    print(State.state_string(side), "Win!")
                self.win_game_collections[side].append(self.export_game_record())
                break
        if not someone_win:
            if render:
                print("Game Drawn!")
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

    def run_experiment(self, game_nums, black_player, white_player, render=False, save_dir=None):
        for _ in range(game_nums):
            self.play_game(black_player=black_player,white_player=white_player,render=render)

        """
        if not save_dir:
            white_path = os.path.join(save_dir, "white_win")
            black_path = os.path.join(save_dir, "black_win")
            draw_path = os.path.join(save_dir, "draw")
            for record in self.win_game_collections:
                with 
        """

        string_dict = {State.Black: "Black Win", State.White: "White Win"}
        print("Results")
        print("total games:", game_nums)
        print("Black:", black_player.name, "White:", white_player.name)
        print("------------")
        for wins in self.win_game_collections:
            print(string_dict[wins], len(self.win_game_collections[wins]), "(", len(self.win_game_collections[wins]) / game_nums,")")
        print("Draw", len(self.drawn_game_collections), "(", len(self.drawn_game_collections) / game_nums,")")
        print("------------")
