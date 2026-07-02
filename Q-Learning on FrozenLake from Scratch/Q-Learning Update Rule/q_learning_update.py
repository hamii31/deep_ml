def q_learning_update(q_table, state, action, reward, next_state, done, alpha, gamma):
    # TODO: apply Q(s,a) += alpha * (target - Q(s,a)) in place and return the new Q value
    target = td_target(reward, gamma, q_table, next_state, done)
    error = td_error(target, q_table, state, action)
    q_table[state][action] += alpha * error
    return q_table[state][action]
