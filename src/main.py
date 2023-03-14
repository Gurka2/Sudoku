from board import init_board, is_legal_move, is_row_valid, is_col_valid, print_board, is_box_valid, solve_sudoku
# coord (6, 1) to (8, 1) is bugged
# it recongizes it is zero but places no value in the square

def main() -> None:
    # board = init_board()
    empty = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            ]
    solve_sudoku(empty)
    print_board(empty)


main()
