import numpy as np

def place_move(board, row, col, player):
    """Place player's mark at (row, col) and return the new board."""
    # TODO: verify the cell is empty, then return a new board with the mark placed.
    if is_cell_empty(board, row, col): 
        board_copy = np.copy(board)
        board_copy[row][col] = player
        return board_copy
    else:
        raise ValueError('Target cell is already occupied.')
