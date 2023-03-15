from board import is_legal_move, is_row_valid, is_col_valid, print_board, is_box_valid, solve_sudoku
from render import *
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
    clear_terminal()
    render_board_at_pos(empty, 0, 0)


main()
