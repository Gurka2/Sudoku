# internal imports
from board import *
from render import clear_terminal, hide_cursor, move_courser_to_pos, render_board_at_pos, render_cursor_pos, show_cursor
from color import Color

# external imports
from typing import Any

# requirements
import getch

class Game():
    """ This class is actually a struct """

    def __init__(self, board_pos_x, board_pos_y):
        self.x: int = 1
        self.board_pos: tuple[int, int] = (board_pos_x, board_pos_y)
        self.cursor_x: int = 8
        self.cursor_y: int = 1
        self.cursor_color: Color = Color.CYAN
        #self.board = init_game_board()
        self.csp_board: list[list[Box]] = init_csp_game_board()
        self.user_input: list[Any] = []
        self.exit: bool = False

def calculate_abs_cursor_pos(cursor_relative_x: int,
                             cursor_relative_y: int,
                             board_pos:         tuple[int, int]
                             ) -> tuple[int, int]:

    cursor_padding_x: int = 2
    cursor_padding_y: int = 1

    cursor_scaling_x: int = 4
    cursor_scaling_y: int = 2

    cursor_abs_x: int = cursor_relative_x * cursor_scaling_x + cursor_padding_x + board_pos[0]
    cursor_abs_y: int = cursor_relative_y * cursor_scaling_y + cursor_padding_y + board_pos[1]

    return (cursor_abs_x, cursor_abs_y)

def handle_cursor_movement(game: Game):
    """ 
    Moves the cursor around the board according to vim keybinds
    without going outside of the board
    """
    user_input: list[str] = game.user_input

    # TODO: DRY
    # TODO: Errors (ignore invalid inputs)
    # TODO: Redraw after mouse moved
    if user_input[-1] == 'h':

        if len(user_input) == 1:
            game.cursor_x = max(0, game.cursor_x - 1)

        else:
            number: str = ''

            for value in user_input[0:-1]:
                number += value

            game.cursor_x = max(0, game.cursor_x - int(number))

    if user_input[-1] == 'l':

        if len(user_input) == 1:
            game.cursor_x = min(8, game.cursor_x + 1)

        else:
            number: str = ''

            for value in user_input[0:-1]:
                number += value
            game.cursor_x = min(8, game.cursor_x + int(number))

    if user_input[-1] == 'j':

        if len(user_input) == 1:
            game.cursor_y = min(8, game.cursor_y + 1)

        else:
            number: str = ''

            for value in user_input[0:-1]:
                number += value
            game.cursor_y = min(8, game.cursor_y + int(number))

    if user_input[-1] == 'k':

        if len(user_input) == 1:
            game.cursor_y = max(0, game.cursor_y - 1)

        else:
            number: str = ''

            for value in user_input[0:-1]:
                number += value

            game.cursor_y = max(0, game.cursor_y - int(number))

def take_user_input() -> list[str]:
    # crashes on anything but esc, letters and number, e.g. ctrl-d => crash
    return [getch.getch()]

def handle_user_input(game: Game):
    user_input = game.user_input[-1]
    
    if user_input in 'qp':
        game.exit = True
    
    if user_input in 'hjkl':
        handle_cursor_movement(game)
        game.user_input = []

    if user_input in '123456789':
        return

def csp_board_to_normal_board(board: list[list[Box]]) -> list[list[int]]:
    return [[box.square for box in row] for row in board]

def init_csp_game_board() -> list[list[Box]]:
    csp_board = init_empty_csp_board()
    init_random_values_csp(csp_board)
    init_boxes(csp_board)

    return csp_board

def start_sudoku(board_pos_x: int, board_pos_y: int):

    # Init game variables
    game = Game(board_pos_x, board_pos_y)

    hide_cursor()

    # Runs the game
    while True:

        # Graphics
        clear_terminal()
        board = csp_board_to_normal_board(game.csp_board)
        render_board_at_pos(board, game.board_pos)
        cursor_abs_pos = calculate_abs_cursor_pos(game.cursor_x,
                                                  game.cursor_y,
                                                  game.board_pos)
        render_cursor_pos(cursor_abs_pos, game.cursor_color)

        game.user_input += take_user_input()
        handle_user_input(game)

        if game.exit:
            break

    show_cursor()
    clear_terminal()


