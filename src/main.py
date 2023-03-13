from board import init_board, is_legal_move, is_row_valid, is_col_valid, place_value, print_board, is_box_valid, solve_sudoku

# coord (6, 1) to (8, 1) is bugged
# it recongizes it is zero but places no value in the square

def main() -> None:
    board = init_board()
    test_board = [
            [i for i in range(1, 10)],
            [4,5,6,1,2,3,0,0,0],
            [8,0,0,0,0,0,0,0,0],
            [0,4,0,0,1,0,0,0,0],
            [0,8,0,0,0,0,7,0,0],
            [7,0,1,5,0,0,0,0,3],
            [9,0,6,0,5,0,4,0,0],
            [0,1,0,0,0,0,0,0,0],
            [0,0,0,3,0,0,0,2,0],
            ]
    easy_board = [
            [9,7,4,6,0,5,0,0,0],
            [2,6,1,7,0,4,5,0,0],
            [8,3,5,2,1,9,7,0,4],

            [0,5,2,1,0,0,6,8,0],
            [0,8,6,0,0,2,0,1,5],
            [3,0,0,5,6,8,0,0,0],

            [0,0,0,0,7,0,2,0,6],
            [0,0,0,8,0,0,3,4,9],
            [5,4,0,0,0,0,0,0,0],
            ]
    print_board(board)
    solve_sudoku(easy_board)
    print(is_legal_move(test_board, 6, 1, 4))
    # print_board(test_board)
    # print_board(board)
    pass


main()
