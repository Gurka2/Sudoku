from board import *

def get_solved_boards() -> tuple[ list[ list[ int ]]]:
    board_one = [
            [1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,1,4,3,6,5,8,9,7],
            [3,6,5,8,9,7,2,1,4],
            [8,9,7,2,1,4,3,6,5],
            [5,3,1,6,4,2,9,7,8],
            [6,4,2,9,7,8,5,3,1],
            [9,7,8,5,3,1,6,4,2],
            ]

    return board_one,

def get_unsolved_boards() -> tuple[ list[ list[ int ]]]:
    board_one = [
            [0,2,3,4,5,6,7,0,9],
            [4,0,6,0,0,9,1,2,3],
            [7,8,9,1,2,3,0,0,6],
            [2,1,4,3,0,5,8,9,7],
            [3,6,5,8,0,7,2,0,4],
            [0,9,0,2,1,4,3,6,5],
            [5,3,1,6,0,2,9,0,8],
            [0,4,2,0,0,8,5,3,1],
            [0,7,8,5,3,1,0,4,2],
            ]

    return board_one,

def input_values_csp_board(board: list[list[Box]]) -> list[list[Box]]:
    values = [1,2,3]
    positions = ((0,0),(1,1),(2,2))
    for i in range(3):
        x = positions[i][0]
        y = positions[i][1]
        board[y][x].square = values[i]
    return board

""" Tests for the regular sudoku representation """

def test_cols(board: list[list[int]], board_index: int):
    for i in range(SIZE):
        assert is_col_valid(board, i) == True, \
        f"Board {board_index} column {i} failed"

def test_rows(board: list[list[int]], board_index: int):
    for i in range(SIZE):
        assert is_row_valid(board, i) == True, \
        f"Board {board_index} column {i} failed"

def test_boxes(board: list[list[int]], board_index: int):
    for i in range(SIZE):
        assert is_box_valid(board, i) == True, \
        f"Board {board_index} column {i} failed"

def test_legal_moves(board: list[list[int]], board_index: int):
    for y in range(SIZE):
        for x in range(SIZE):
            current_number: int = board[y][x]
            assert is_legal_move(board, x, y, current_number) == True, \
            f"Board {board_index} failed at \
              placing {current_number} at ({x}, {y})"

""" Tests for the csp sudoku representation """

def csp_empty_board(board: list[list[Box]]):
    for y in range(SIZE):
        for x in range(SIZE):
            assert board[y][x].value == 0, f"Empty board {x, y} is not zero"

def test_csp_row(board: list[list[Box]], y: int):
    row = board[y]
    values_in_row = [box.square for box in row if box.square != 0]
    for box in row:
        assert box.constraints.sort() == values_in_row.sort(), \
        f"Box constraints = {box.constraints} \
          Values it should contain: {values_in_row}"

def test_csp_col(board: list[list[Box]], x: int):
    pass

def test_csp_block(board: list[list[Box]], block: tuple[int, int]):
    pass

def test():
    solved = get_solved_boards()
    
    for i, board in enumerate(solved):
        test_cols(board, i)
        test_rows(board, i)
        test_boxes(board, i)
        test_legal_moves(board, i)

    unsolved = get_unsolved_boards()
    
    for i, board in enumerate(unsolved):
        test_cols(board, i)
        test_rows(board, i)
        test_boxes(board, i)
        test_legal_moves(board, i)

    print("All test successful")

def test_csp():
    empty_board = init_empty_csp_board()
    board_one = input_values_csp_board(empty_board)

    for i in range(SIZE):
        test_csp_row(board_one, i)
        test_csp_col(board_one, i)

        y = i%3 * 3
        x = i//3 * 3
        test_csp_block(board_one, (x,y))

    print("All csp test successful")


if __name__ == "__main__":
    test()
    test_csp()
