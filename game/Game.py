from game.Board import Board

#    0  1  2  3  4  5  6
# 0 [ ][ ][ ][ ][ ][ ][ ]
# 1 [ ][ ][ ][ ][ ][ ][ ]
# 2 [ ][ ][ ][ ][ ][ ][ ]
# 3 [ ][ ][ ][ ][ ][ ][ ]
# 4 [ ][ ][ ][ ][ ][ ][ ]
# 5 [ ][ ][ ][ ][ ][ ][ ]


class Game:
    def __init__(self, board_size, player_a, player_b):
        self.board = Board(board_size)
        self.player_a = player_a
        self.player_b = player_b
        self.player_a_turn = True

    def _check_win(self, last_played_pos):
        possible_offsets = [
            [[1, 0], [2, 0], [3, 0]],
            [[-1, 0], [1, 0], [2, 0]],
            [[0, 1], [0, 2], [0, 3]],
            [[1, 1], [2, 2], [3, 3]],
            [[-1, -1], [1, 1], [2, 2]],
            [[-2, -2], [-1, -1], [1, 1]],
            [[1, -1], [2, -2], [3, -3]],
            [[-1, 1], [1, -1], [2, -2]],
            [[-2, 2], [-1, 1], [1, -1]],
        ]

        c = last_played_pos[0]
        r = last_played_pos[1]
        b = self.board

        for offset in possible_offsets:
            if b.get(c, r) == b.get(c+offset[0][0], r+offset[0][1]) == b.get(c+offset[1][0], r+offset[1][1]) == b.get(c+offset[2][0], r+offset[2][1]):
                return True

            if b.get(c, r) == b.get(c-offset[0][0], r-offset[0][1]) == b.get(c-offset[1][0], r-offset[1][1]) == b.get(c-offset[2][0], r-offset[2][1]):
                return True

        return False

    def get_current_player(self):
        return self.player_a if self.player_a_turn else self.player_b

    def play(self, columnIndex):
        player = self.get_current_player()
        if columnIndex not in self.board.available_columns():
            return

        rowIndex = self.board.placeInColumn(columnIndex, player.symbol)
        win = self._check_win([columnIndex, rowIndex])
        self.player_a_turn = not self.player_a_turn
        return win

    def print(self):
        self.board.print()
