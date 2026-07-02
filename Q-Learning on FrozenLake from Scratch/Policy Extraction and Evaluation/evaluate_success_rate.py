def evaluate_success_rate(env, policy, num_episodes, seed=0, max_steps=200):
    # TODO: run num_episodes greedy rollouts and return the fraction that reached the goal.
    env.reset(seed=seed)
    env.action_space.seed(seed)

    success = 0
    for episode in range(num_episodes):
        reached_goal = run_greedy_episode(env, policy, seed=seed + episode, max_steps=max_steps)
        success += reached_goal / num_episodes

    return success
