# internal
from board import init_empty_board, solve_sudoku
from render import clear_terminal, hide_cursor, move_courser_to_pos, render_board_at_pos, render_cursor_pos, show_cursor
from color import Color

# external
from typing import Any

# requirements
import getch

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

def handle_cursor_movement(game: dict[str, Any]):
    """ 
    Moves the cursor around the board according to vim keybinds
    without going outside of the board
    """
    user_input: list[str] = game['user_input']

    # TODO: DRY
    if user_input[-1] == 'h':

        if len(user_input) == 1:
            game['cursor_x'] = max(0, game['cursor_x'] - 1)

        else:
            number: str = ''

            for value in user_input[0:-1]:
                number += value

            game['cursor_x'] = max(0, game['cursor_x'] - int(number))

    if user_input[-1] == 'l':

        if len(user_input) == 1:
            game['cursor_x'] = min(8, game['cursor_x'] + 1)

        else:
            number: str = ''

            for value in user_input[0:-1]:
                number += value
            game['cursor_x'] = min(8, game['cursor_x'] + int(number))

    if user_input[-1] == 'j':

        if len(user_input) == 1:
            game['cursor_y'] = min(8, game['cursor_y'] + 1)

        else:
            number: str = ''

            for value in user_input[0:-1]:
                number += value
            game['cursor_y'] = min(8, game['cursor_y'] + int(number))

    if user_input[-1] == 'k':

        if len(user_input) == 1:
            game['cursor_y'] = max(0, game['cursor_y'] - 1)

        else:
            number: str = ''

            for value in user_input[0:-1]:
                number += value

            game['cursor_y'] = max(0, game['cursor_y'] - int(number))

def take_user_input() -> list[str]:
    # crashes on anything but esc, letters and number, e.g. ctrl-d => crash
    return [getch.getch()]

def handle_user_input(game: dict[str, Any]):
    user_input = game['user_input'][-1]
    
    if user_input in 'qp':
        game['exit'] = True
    
    if user_input in 'hjkl':
        handle_cursor_movement(game)
        game['user_input'] = []

    if user_input in '123456789':
        return

def start_sudoku(board_pos_x: int, board_pos_y: int):

    # Init game variables, and this is a struct
    game = {
    'board_pos': (board_pos_x, board_pos_y),
    'cursor_x': 8,
    'cursor_y': 1,
    'cursor_color': Color.CYAN,
    'board': init_empty_board(),
    'user_input': [],
    'exit': False}

    solve_sudoku(game['board'])

    hide_cursor()

    # Runs the game
    while True:

        # Graphics
        clear_terminal()
        render_board_at_pos(game['board'], game['board_pos'])
        cursor_abs_pos = calculate_abs_cursor_pos(game['cursor_x'], game['cursor_y'], game['board_pos'])
        render_cursor_pos(cursor_abs_pos, game['cursor_color'])

        game['user_input'] += take_user_input()
        handle_user_input(game)

        if game['exit']:
            break

    show_cursor()


