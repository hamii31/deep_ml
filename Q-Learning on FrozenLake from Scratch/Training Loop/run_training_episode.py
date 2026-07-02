def run_training_episode(env, q_table, epsilon, alpha, gamma, rng, max_steps=200):
    # TODO: reset env, then repeatedly call interaction_step until done or max_steps, returning total reward.
    current_obs, _ = env.reset()
    total_reward = 0
    for i in range(max_steps):
        current_obs, current_reward, done = interaction_step(env, q_table, current_obs, epsilon, alpha, gamma, rng)
        total_reward += current_reward
        if done:
            break

    return total_reward
