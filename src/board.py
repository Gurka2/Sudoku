from random import randrange

SIZE                       = 9
ROW_SEPARATOR              = "+---+---+---+---+---+---+---+---+---+"

def init_board() -> list[list[int]]:
    board = [ [ 0 for _ in range(9)] for _ in range(9) ]
    return board

def print_board(board: list[list[int]]) -> None:
    pp_board = ROW_SEPARATOR + "\n"
    for y in range(SIZE):
        row = "| "

        for x in range(SIZE):
            row += str(board[y][x]) + " | "

        pp_board += row + "\n"
        pp_board += ROW_SEPARATOR + "\n"

    print(pp_board)

def place_value(board: list[list[int]], x: int, y: int, value: int) -> None:
    board[y][x] = value

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

def solve_sudoku(board: list[list[int]]) -> None:
    print_board(board)

    for y in range(SIZE):
        for x in range(SIZE):
            values: list[int] = [i for i in range(1, 10)]

            if board[y][x] == 0:
                for value in values:
                    if is_legal_move(board, x, y, value):
                        board[y][x] = value

                        solve_sudoku(board)

                board[y][x] = 0
                print(f"x: {x} y: {y}")
                return




