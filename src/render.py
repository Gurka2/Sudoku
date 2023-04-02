from color import Color

BIG_RIGHT_UPPER_CORNER  = '╔'
BIG_RIGHT_LOWER_CORNER  = '╚'
BIG_LEFT_UPPER_CORNER   = '╗'
BIG_LEFT_LOWER_CORNER   = '╝'
BIG_HORIZONTAL          = '═'
BIG_VERTICAL            = '║'
BIG_CROSS               = '╬'
BIG_VERITCAL_RIGHT      = '╠'
BIG_VERITCAL_LEFT       = '╣'

SMAL_RIGHT_UPPER_CORNER = '┌'
SMAL_RIGHT_LOWER_CORNER = '└'
SMAL_LEFT_UPPER_CORNER  = '┐'
SMAL_LEFT_LOWER_CORNER  = '┘'
SMAL_HORIZONTAL         = '─'
SMAL_VERTICAL           = '│'
SMAL_CROSS              = '┼'

TOP_ROW                 = BIG_RIGHT_UPPER_CORNER + 35*BIG_HORIZONTAL + BIG_LEFT_UPPER_CORNER
BOT_ROW                 = BIG_RIGHT_LOWER_CORNER + 35*BIG_HORIZONTAL + BIG_LEFT_LOWER_CORNER
SMAL_ROW_SEPARATOR      = BIG_VERTICAL + 3*(3*SMAL_HORIZONTAL + SMAL_CROSS + 3*SMAL_HORIZONTAL + SMAL_CROSS + 3*SMAL_HORIZONTAL + BIG_VERTICAL)
BIG_ROW_SEPARATOR       = BIG_VERITCAL_RIGHT + 2*(11*BIG_HORIZONTAL + BIG_CROSS) + 11*BIG_HORIZONTAL + BIG_VERITCAL_LEFT

SIZE = 9

ESC     = '\033'
CTRL    = '['
PADDING = ' '

def print_ANSI_code(code: str):
    print(ESC+CTRL+code, end='')

def change_color(color: Color):
    """ changes the color the comming text will be desplayed in """
    print_ANSI_code('1;3' + color.value + 'm')

def move_courser_to_pos(x: int, y: int):
    print_ANSI_code(str(y) + ';' + str(x) + 'f')

def clear_terminal():
    print_ANSI_code('2J')

def hide_cursor():
    print_ANSI_code('?25l')

def show_cursor():
    print_ANSI_code('?25h')

def print_at_pos(x: int, y: int, string: str):
    """ Prints given string at given position.
        x and y increased since 0 is equal to 1 by default. """
    x += 1
    y += 1
    move_courser_to_pos(x, y)
    print(string)

def print_at_pos_color(x: int, y: int, string: str, color: Color):
    """ Prints given string at given position with given color.
        x and y increased since 0 is equal to 1 by default. """
    change_color(color)
    print_at_pos(x, y, string)
    change_color(Color.WHITE)

def render_cursor_pos(cursor_abs_pos: tuple[int, int], cursor_color: Color):
    cursor_abs_x, cursor_abs_y = cursor_abs_pos

    # TODO: clean up
    # TODO: and decide whether to use tuples and lists or dictionaries
    top_row_pos: dict[str, int] = {'x': cursor_abs_x-2, 'y': cursor_abs_y-1}
    bot_row_pos: dict[str, int] = {'x': cursor_abs_x-2, 'y': cursor_abs_y+1}
    mid_row_pos: tuple[dict[str, int], dict[str, int]] = ({'x': cursor_abs_x-2, 'y': cursor_abs_y},
                                                          {'x': cursor_abs_x+2, 'y': cursor_abs_y})
    print_at_pos_color(top_row_pos['x'], top_row_pos['y'], '╔═══╗', cursor_color)
    print_at_pos_color(bot_row_pos['x'], bot_row_pos['y'], '╚═══╝', cursor_color)

    for pos in mid_row_pos:
        print_at_pos_color(pos['x'], pos['y'], '║', cursor_color)

def render_board_at_pos(board: list[list[int]], board_pos: tuple[int, int]):
    _x = board_pos[0]
    _y = board_pos[1]

    print_at_pos(_x, _y, TOP_ROW)
    for y in range(SIZE):
        row: str = BIG_VERTICAL + PADDING 

        for x in range(SIZE):
            if x%3 != 2:
                row += str(board[y][x]) + PADDING + SMAL_VERTICAL + PADDING
            else:
                row += str(board[y][x]) + PADDING + BIG_VERTICAL + PADDING

        _y += 1
        row = row[0:-2] + BIG_VERTICAL # Python didn't let me to row[-1] = ... 
        print_at_pos(_x, _y, row)

        _y += 1
        if y%3 != 2:
            print_at_pos(_x, _y, SMAL_ROW_SEPARATOR)
        elif y == 8:
            print_at_pos(_x, _y, BOT_ROW)
        else:
            print_at_pos(_x, _y, BIG_ROW_SEPARATOR)
