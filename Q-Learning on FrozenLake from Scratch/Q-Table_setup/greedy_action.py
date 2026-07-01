import numpy as np

def greedy_action(q_table, state):
    """Return the action index with the highest Q value at the given state."""
    # TODO: return argmax over the action axis for this state's Q values
    return int(np.argmax(q_table[state]))
