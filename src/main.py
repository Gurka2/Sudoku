from board import init_board, is_legal_move, is_row_valid, is_col_valid, place_value, print_board, is_box_valid, solve_sudoku

def main() -> None:
    board = init_board()
    solve_sudoku(board)
    print_board(board)
    pass


main()
