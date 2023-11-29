from game.Board import Board

#  0  1  2  3  4  5  6
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]


class Game:
    def __init__(self, board_size, player_a, player_b):
        self.board = Board(board_size)
        self.player_a = player_a
        self.player_b = player_b
        self.player_a_turn = True

    # Gayatri im writing the other way
    def _check_win(self, last_played_pos):
        c = last_played_pos[0]
        r = last_played_pos[1]
        b = self.board

        # does not work yet for instances where last played coin in not in at the end of the 4

        # up from last played coin
        if b.get(c, r) == b.get(c+1, r) == b.get(c+2, r) == b.get(c+3, r):
            return True

        # down from last played coin
        if b.get(c, r) == b.get(c-1, r) == b.get(c-2, r) == b.get(c-3, r):
            return True

        # right from last played coin
        if b.get(c, r) == b.get(c, r+1) == b.get(c, r+2) == b.get(c, r+3):
            return True

        # left from last played coin
        if b.get(c, r) == b.get(c, r-1) == b.get(c, r-2) == b.get(c, r-3):
            return True

        # top-right from last played coin
        if b.get(c, r) == b.get(c+1, r+1) == b.get(c+2, r+2) == b.get(c+3, r+3):
            return True

        # bottom-right from last played coin
        if b.get(c, r) == b.get(c+1, r-1) == b.get(c+2, r-2) == b.get(c+3, r-3):
            return True

        # top-left from last played coin
        if b.get(c, r) == b.get(c-1, r+1) == b.get(c-2, r+2) == b.get(c-3, r+3):
            return True

        # bottom-left from last played coin
        if b.get(c, r) == b.get(c-1, r-1) == b.get(c-2, r-2) == b.get(c-3, r-3):
            return True

        return False

    def current_player(self):
        return self.player_a if self.player_a_turn else self.player_b

    def play(self, columnIndex, player):
        if columnIndex not in self.board.available_columns():
            return

        rowIndex = self.board.placeInColumn(columnIndex, player.symbol)
        win = self._check_win([columnIndex, rowIndex])
        self.player_a_turn = not self.player_a_turn
        return win

    def print(self):
        self.board.print()
