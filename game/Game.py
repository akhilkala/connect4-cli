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

    def _check_win(self, player):
        symbol = player.symbol
        win = False

        # vertical checker
        print("vertical check", win)
        for row in range(5):
            for col in range(4):
                print(row, col)
                print(self.board[1][0])
                print(self.board[1][1])
                print(self.board[1][2])
                print(self.board[1][4])
                if self.board[row][col] == symbol:
                    win = win or self.board[row][col] == self.board[row][col +
                                                                         1] == self.board[row][col+2] == self.board[col+3]

        # horizontal checker
        print("horizontal check", win)
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == symbol:
                    win = win or self.board[row][col] == self.board[row +
                                                                    1][col] == self.board[row+2][col] == self.board[row+3][col]

        print("positive diagonal check", win)
        # positive diagonal checker
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == symbol:
                    win = win or self.board[row][col] == self.board[row+1][col +
                                                                           1] == self.board[row+2][col+2] == self.board[row+3][col+3]

        print("negative diagonal check", win)
        # negative diagonal checker
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == symbol:
                    win = win or self.board[row][col] == self.board[row+1][col -
                                                                           1] == self.board[row+2][col-2] == self.board[row+3][col-3]

        return win

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

        for i, element in enumerate(self.board[columnIndex]):
            if element == Game._EMPTY_SYMBOL:
                self.board[columnIndex][i] = player.symbol
                break
        win = self._check_win(player)
        self.player_a_turn = not self.player_a_turn
        return win

    def print(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row])
              for row in self.board]))
