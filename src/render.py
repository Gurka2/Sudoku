# https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_(Control_Sequence_Introducer)_sequences
# ESC CTRL CODE
# Ex: '\033[A
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

def print_ANSI_code(code: str):
    print(ESC+CTRL+code, end='')

def move_courser_to_pos(x: int, y: int):
    print_ANSI_code(str(y) + ';' + str(x) + 'f')

def clear_terminal():
    print_ANSI_code('2J')

def print_at_pos(x: int, y: int, string: str):
    """ Prints given string at given position.
        x and y increased since 0 is equal to 1 by default. """
    x += 1
    y += 1
    move_courser_to_pos(x, y)
    print(string)

def render_board_at_pos(board: list[list[int]], _x: int, _y: int):

    print_at_pos(_x, _y, TOP_ROW)
    for y in range(SIZE):
        row: str = BIG_VERTICAL + ' '

        for x in range(SIZE):
            if x%3 != 2:
                row += str(board[y][x]) + ' ' + SMAL_VERTICAL + ' '
            else:
                row += str(board[y][x]) + ' ' + BIG_VERTICAL + ' '

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




