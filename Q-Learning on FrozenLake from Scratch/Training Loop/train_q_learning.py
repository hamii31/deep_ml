import numpy as np

def train_q_learning(env, num_episodes, alpha=0.1, gamma=0.99, epsilon_start=1.0, epsilon_min=0.05, epsilon_decay=0.999, seed=0, max_steps=200):
    # TODO: train a Q-learning agent for num_episodes; return (q_table, returns)
    rng = np.random.default_rng(seed)
    env.reset(seed=seed)
    env.action_space.seed(seed)

    n_states = env.observation_space.n
    n_actions = env.action_space.n
    q_table = init_q_table(n_states, n_actions)

    episode_returns = []
    epsilon = epsilon_start
    for episode in range(num_episodes):
        total_reward = run_training_episode(env, q_table, epsilon, alpha, gamma, rng, max_steps=200)
        episode_returns.append(total_reward)
        epsilon = decay_epsilon(epsilon, epsilon_decay, epsilon_min)

    return (q_table, episode_returns)
