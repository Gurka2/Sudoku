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

def test_cols(board: list[list[int]], board_index: int):
    for i in range(SIZE):
        assert is_col_valid(board, i) == True, f"Board {board_index} column {i} failed"

def test_rows(board: list[list[int]], board_index: int):
    for i in range(SIZE):
        assert is_row_valid(board, i) == True, f"Board {board_index} column {i} failed"

def test_boxes(board: list[list[int]], board_index: int):
    for i in range(SIZE):
        assert is_box_valid(board, i) == True, f"Board {board_index} column {i} failed"

def test_legal_moves(board: list[list[int]], board_index: int):
    for y in range(SIZE):
        for x in range(SIZE):
            current_number: int = board[y][x]
            assert is_legal_move(board, x, y, current_number) == True, f"Board {board_index} failed at \
                                                                         placing {current_number} at ({x}, {y})"

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

if __name__ == "__main__":
    test()
