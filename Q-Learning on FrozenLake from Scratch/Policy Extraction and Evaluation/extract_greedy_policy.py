def extract_greedy_policy(q_table):
    # TODO: return a 1D int64 array mapping each state to its best (argmax) action.
    policy = np.empty(shape=len(q_table), dtype=np.int64)
    N = len(q_table)
    for state in range(N):
        policy[state]=greedy_action(q_table, state)

    return policy
