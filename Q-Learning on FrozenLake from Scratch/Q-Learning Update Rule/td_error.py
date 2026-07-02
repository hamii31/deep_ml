def td_error(target, q_table, state, action):
    # TODO: return the TD error: target minus current Q(state, action)
    return target - q_table[state][action]
