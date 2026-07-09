import numpy as np

def print_board(board):
    """Print the 3x3 board using X, O, and . characters."""
    # TODO: render each cell as 'X' (1), 'O' (-1), or '.' (0) in a 3x3 grid
    for row in board:
        new_row = []
        for cell in row:
            if cell == 1: new_row.append('X')
            elif cell == -1: new_row.append('O')
            elif cell == 0: new_row.append('.')
        print(" ".join(new_row))
