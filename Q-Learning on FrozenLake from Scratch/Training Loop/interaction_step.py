def interaction_step(env, q_table, state, epsilon, alpha, gamma, rng):
    # TODO: select epsilon-greedy action, step env, apply Q-learning update, return (next_state, reward, done)
    new_action = epsilon_greedy_action(q_table, state, epsilon, env.action_space, rng)
    obs, reward, terminated, truncated , info = env.step(new_action)
    q_table = q_learning_update(q_table, state, new_action, reward, obs, terminated, alpha, gamma)
    return (int(obs), float(reward), bool(terminated))
