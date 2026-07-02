def run_greedy_episode(env, policy, seed=None, max_steps=200):
    """Run one greedy episode and return True if the goal was reached."""
    current_obs, _ = env.reset(seed=seed)
    total_reward = 0
    for _ in range(max_steps):
        action = int(policy[current_obs])
        current_obs, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        done = terminated or truncated
        if done:
            break
    return total_reward > 0
