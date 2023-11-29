from game.Player import *

#  0  1  2  3  4  5  6
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ]


class Game:
    _EMPTY_SYMBOL = "_"

    def __init__(self, board_size, player_a, player_b):
        self.board = self._create_board(board_size)
        self.player_a = player_a
        self.player_b = player_b
        self.player_a_turn = True

    def _create_board(self, board_size):
        rows = board_size[0]
        columns = board_size[1]
        board = []
        for col in range(columns):
            col = []
            for _ in range(rows):
                col.append(Game._EMPTY_SYMBOL)
            board.append(col)
        return board

    # Gayatri im writing the other way
    def _check_win(self, last_played_pos):
        number_of_cols = len(self.board)
        number_of_rows = len(self.board[0])
        won = False

        c = last_played_pos[0]
        r = last_played_pos[1]
        b = self.board
        for _ in range(4):
            if c + 3 < number_of_cols:
                won = won or b[c][r] == b[c+1][r] == b[c+2][r] == b[c+3][r]
            if c - 3 >= 0:
                won = won or b[c][r] == b[c-1][r] == b[c-2][r] == b[c-3][r]
            if r + 3 < number_of_rows:
                won = won or b[c][r] == b[c][r+1] == b[c][r+2] == b[c][r+3]
            if r - 3 >= 0:
                won = won or b[c][r] == b[c][r-1] == b[c][r-2] == b[c][r-3]
            if c + 3 < number_of_cols and r + 3 < number_of_rows:
                won = won or b[c][r] == b[c+1][r +
                                               1] == b[c+2][r+2] == b[c+3][r+3]
            if c + 3 < number_of_cols and r - 3 >= 0:
                won = won or b[c][r] == b[c+1][r -
                                               1] == b[c+2][r-2] == b[c+3][r-3]
            if c - 3 >= 0 and r + 3 < number_of_rows:
                won = won or b[c][r] == b[c-1][r +
                                               1] == b[c-2][r+2] == b[c-3][r+3]
            if c - 3 >= 0 and r - 3 >= 0:
                won = won or b[c][r] == b[c-1][r -
                                               1] == b[c-2][r-2] == b[c-3][r-3]
        return won

    def current_player(self):
        return self.player_a if self.player_a_turn else self.player_b

    def available_columns(self):
        cols = []
        number_of_rows = len(self.board[0])
        for i, col in enumerate(self.board):
            col_size = len(list(filter((Game._EMPTY_SYMBOL).__ne__, col)))
            if col_size != number_of_rows:
                cols.append(i)
        return cols

    def play(self, columnIndex, player):
        if columnIndex not in self.available_columns():
            return

        rowIndex = -1
        for i, element in enumerate(self.board[columnIndex]):
            if element == Game._EMPTY_SYMBOL:
                self.board[columnIndex][i] = player.symbol
                rowIndex = i
                break
        win = self._check_win([columnIndex, rowIndex])
        self.player_a_turn = not self.player_a_turn
        return win

    def print(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row])
              for row in self.board]))
