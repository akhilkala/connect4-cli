class Board:
    _EMPTY_SYMBOL = "_"

    def __init__(self, board_size):
        self._board = self._create(board_size)
        self.number_of_rows = board_size[0]
        self.number_of_cols = board_size[1]

    def _create(self, board_size):
        rows = board_size[0]
        columns = board_size[1]
        board = []
        for col in range(columns):
            col = []
            for _ in range(rows):
                col.append(Board._EMPTY_SYMBOL)
            board.append(col)
        return board

    def available_columns(self):
        cols = []
        number_of_rows = len(self._board[0])
        for i, col in enumerate(self._board):
            col_size = len(list(filter((Board._EMPTY_SYMBOL).__ne__, col)))
            if col_size != number_of_rows:
                cols.append(i)
        return cols

    def placeInColumn(self, index, symbol):
        rowIndex = -1
        for i, element in enumerate(self._board[index]):
            if element == Board._EMPTY_SYMBOL:
                self._board[index][i] = symbol
                rowIndex = i
                break
        return rowIndex

    def get(self, col, row):
        if col < 0 or col >= self.number_of_cols or row < 0 or row >= self.number_of_rows:
            return None
        return self._board[col][row]

    def print(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row])
              for row in self._board]))
