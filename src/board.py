from random import randrange

SIZE = 9

class Solutions():
    boards = []


class Box():
    def __init__(self):
        self.square = 0
        self.constraints: list[int] = []


def init_empty_board() -> list[list[int]]:
    board = [[ 0 for _ in range(9)] for _ in range(9)]
    return board

def is_row_valid(board: list[list[int]], y: int) -> bool:
    # Why not just check for doubles?
    values: list[int] = [i for i in range(1,10)]

    for number in board[y]:
        if number in values:
            values.remove(number)

        elif number != 0 and number not in values:
            return False

    return True

def is_col_valid(board: list[list[int]], x: int) -> bool:
    # Why not just check for doubles?
    values: list[int] = [i for i in range(1,10)]

    for i in range(9):
        number = board[i][x]

        if number in values:
            values.remove(number)

        elif number != 0 and number not in values:
            return False

    return True

def is_box_valid(board: list[list[int]], box: int) -> bool:
    # Why not just check for doubles?
    board_box = [ ((box%3)*3 + (i%3),(box//3)*3 + (i//3)) \
                 for i in range(9) ]
    values = [i for i in range(1, 10)]

    for x,y in board_box:
        number = board[y][x]
        
        if number in values:
            values.remove(number)

        elif number != 0 and number not in values:
            return False

    return True

def is_solved(board: list[list[int]]) -> bool:

    for y in range(SIZE):
        for x in range(SIZE):
            if board[y][x] == 0:
                return False

    for i in range(SIZE):
        if not is_box_valid(board, i) or \
        not is_col_valid(board, i) or \
        not is_row_valid(board, i):
            return False

    return True

def is_legal_move(board: list[list[int]], x: int, \
                  y: int, number: int) -> bool:
    current_number: int = board[y][x]
    board[y][x] = number 
    valid = None
    box: int = (x//3) + (y//3) * 3

    if is_col_valid(board, x) \
    and is_row_valid(board, y) \
    and is_box_valid(board, box):
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

def get_total_solutions(board: list[list[int]], solutions: Solutions):
    print(len(solutions.boards))
    print(solutions.boards)
    for y in range(SIZE):
        for x in range(SIZE):

            if board[y][x] == 0:
                values: list[int] = [i for i in range(1, 10)]

                for value in values:
                    if is_legal_move(board, x, y, value):

                        board[y][x] = value
                        get_total_solutions(board, solutions)
                        if is_solved(board):
                            if board in solutions.boards:
                                solutions.boards.append(board)
                            return

                board[y][x] = 0
                return

def solve_sudoku_csp(board: list[list[Box]]):
    pass

def init_csp_board(board: list[list[int]]):
    pass

def init_boxes(board: list[list[Box]]):
    for i in range(9):
        block = (i//3)*3, (i%3)*3
        init_csp_row(i, board)
        init_csp_col(i, board)
        init_csp_block(block, board)

def init_csp_row(row: int, board: list[list[Box]]):
    boxes = board[row]
    add_boxes_constaints(boxes)

def init_csp_col(col: int, board: list[list[Box]]):
    boxes = [board[i][col] for i in range(9)]
    add_boxes_constaints(boxes)

def init_csp_block(block: tuple[int, int], board: list[list[Box]]):
    boxes = []
    for i in range(9):
        row = i%3 + block[1]
        col = i//3 + block[0]
        boxes.append(board[row][col])
    add_boxes_constaints(boxes)

def add_boxes_constaints(boxes: list[Box]):
    values = [box.square for box in boxes if box.square != 0]
    for box in boxes:
        add_box_constraints(box, values)

def add_box_constraints(box: Box, values: list[int]):
    for value in values:
        if value not in box.constraints:
            box.constraints.append(value)

def init_empty_csp_board() -> list[list[Box]]:
    return [[Box() for _ in range(9)] for _ in range(9)]

def remove_random_values(board: list[list[int]], number: int):
    while number > 0:
        x = randrange(0,9)
        y = randrange(0,9)

        if board[y][x] != 0:
            board[y][x] = 0
            number -= 1

def init_random_values_csp(board: list[list[Box]]): 
    # TODO: remove posiblity for sudoku rules to be violated
    for _ in range(2):
        x = randrange(0,9)
        y = randrange(0,9)
        board[y][x].square = randrange(1,10)
    
def create_random_solved_sudoku(board: list[list[int]]):
    # Set five random values in random positions
    for _ in range(20):
        x = randrange(0,9)
        y = randrange(0,9)
        board[y][x] = randrange(1,10)

    # solve_sudoku(board)

def solve_csp_sudoku(board: list[list[Box]]):
    pass


