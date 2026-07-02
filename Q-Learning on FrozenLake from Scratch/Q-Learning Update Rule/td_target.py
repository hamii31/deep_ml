def td_target(reward, gamma, q_table, next_state, done):
    # TODO: compute r + gamma * max_a Q(next_state, a), zeroing the bootstrap when done.
    if not done: return reward + gamma * max_q_value(q_table, next_state)

    return reward
