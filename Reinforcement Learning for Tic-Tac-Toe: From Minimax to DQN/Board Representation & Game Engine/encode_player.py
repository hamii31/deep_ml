def encode_player(player):
    """Return the integer encoding for 'X', 'O', or 'empty'."""
    # TODO: map 'X' to 1, 'O' to -1, 'empty' to 0
    if player == 'X': return 1
    elif player == 'O': return -1
    elif player == 'empty': return 0
