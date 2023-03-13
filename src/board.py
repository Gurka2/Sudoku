from random import randrange

class Board():
    def __init__(self):
        self.SIZE = 9
        self.ROW_SEPARATOR = "+---+---+---+---+---+---+---+---+---+"
        self.board = [ [0 for x in range(9)] for y in range(9) ]
        self._init_board()
        self._solve_sudoku()

    def _init_board(self) -> None:
        x: int = randrange(9)
        y: int = randrange(9)
        self.board[y][x] = randrange(1, 10)

    def print_board(self) -> None:
        board = self.ROW_SEPARATOR + "\n"
        for y in range(self.SIZE):
            row = "| "

            for x in range(self.SIZE):
                row += str(self.board[y][x]) + " | "

            board += row + "\n"
            board += self.ROW_SEPARATOR + "\n"

        print(board)

    def place_value(self, x: int, y: int, value: int) -> None:
        self.board[y][x] = value

    def _is_row_valid(self, y: int) -> bool:
        values = [i for i in range(1,10)]

        for number in self.board[y]:
            if number in values:
                values.remove(number)
            if number != 0 and number not in values:
                return False
        return True

    def _is_col_valid(self, x: int) -> None:
        values = [i for i in range(1,10)]

        for i in range(9):
            number = self.board[i][x]
            if number in values:
                values.remove(number)
            if number != 0 and number not in values:
                return False
        return True

    def _solve_sudoku(self, values: list[int]):

        for y in range(self.SIZE):
            for x in range(self.SIZE):
                if self.board[y][x] == 0 and len(values) > 0:
                    self.board[y][x] = values.pop(0)
                elif self.board[y][x] == 0:
                    return


