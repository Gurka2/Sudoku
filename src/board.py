from random import randrange

SIZE                       = 9

def init_empty_board() -> list[list[int]]:
    board = [ [ 0 for _ in range(9)] for _ in range(9) ]
    return board

def is_row_valid(board: list[list[int]], y: int) -> bool:
    values: list[int] = [i for i in range(1,10)]

    for number in board[y]:

        if number in values:
            values.remove(number)

        elif number != 0 and number not in values:
            return False

    return True

def is_col_valid(board: list[list[int]], x: int) -> bool:
    values: list[int] = [i for i in range(1,10)]

    for i in range(9):
        number = board[i][x]

        if number in values:
            values.remove(number)

        elif number != 0 and number not in values:
            return False

    return True

def is_box_valid(board: list[list[int]], box: int) -> bool:
    board_box = [ ((box%3)*3 + (i%3),(box//3)*3 + (i//3)) for i in range(9) ]
    values = [i for i in range(1, 10)]

    for x,y in board_box:
        number = board[y][x]
        
        if number in values:
            values.remove(number)

        elif number != 0 and number not in values:
            return False

    return True

def is_solved(board: list[list[int]]) -> bool:

    for i in range(SIZE):
        if not is_box_valid(board, i) or not is_col_valid(board, i) or \
        not is_row_valid(board, i):
            return False

    for y in range(SIZE):
        for x in range(SIZE):
            if board[y][x] == 0:
                return False

    return True


def is_legal_move(board: list[list[int]], x: int, y: int, number: int) -> bool:
    current_number: int = board[y][x]
    board[y][x] = number 
    valid = None
    box: int = (x//3) + (y//3) * 3

    if is_col_valid(board, x) and is_row_valid(board, y) and is_box_valid(board, box):
        valid = True
    else:
        valid = False

    board[y][x] = current_number
    return valid

def solve_sudoku(board: list[list[int]]):
    for y in range(SIZE):
        for x in range(SIZE):

            if board[y][x] == 0:
                values: list[int] = [i for i in range(1, 10)]

                for value in values:
                    if is_legal_move(board, x, y, value):

                        board[y][x] = value
                        solve_sudoku(board)
                        if is_solved(board):
                            return

                board[y][x] = 0
                return


