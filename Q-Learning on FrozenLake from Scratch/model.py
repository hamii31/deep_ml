"""
Q-Learning on FrozenLake from Scratch — assembled scaffold.
This updates live as you solve each step.
"""
import numpy as np
import gymnasium as gym

def init_q_table(num_states, num_actions):
    """Return a zero-initialized Q-table of shape (num_states, num_actions)."""
    # TODO: build a 2D float64 numpy array of zeros sized by states and actions.
    return np.zeros(shape=(num_states,num_actions))

def max_q_value(q_table, state):
    """Return the maximum Q value across all actions for the given state."""
    # TODO: index the row for `state` and return its maximum value
    return max(q_table[state])

def greedy_action(q_table, state):
    """Return the action index with the highest Q value at the given state."""
    # TODO: return argmax over the action axis for this state's Q values
    return int(np.argmax(q_table[state]))

def sample_random_action(action_space):
    # TODO: draw a uniformly random action from the given Gymnasium action space
    return int(action_space.sample())

def should_explore(epsilon, rng):
    """Return True with probability epsilon using the provided numpy Generator."""
    # TODO: draw a uniform sample from rng and compare it to epsilon
    return epsilon > rng.random()

def epsilon_greedy_action(q_table, state, epsilon, action_space, rng):
    """Return an epsilon-greedy action for the given state."""
    # TODO: with prob epsilon explore via action_space, else take greedy action
    if should_explore(epsilon, rng):
        return sample_random_action(action_space)
    
    return greedy_action(q_table, state)

def decay_epsilon(epsilon, decay_rate, min_epsilon):
    # TODO: return max(min_epsilon, epsilon * decay_rate)
    return max(min_epsilon, epsilon * decay_rate)

def td_target(reward, gamma, q_table, next_state, done):
    # TODO: compute r + gamma * max_a Q(next_state, a), zeroing the bootstrap when done.
    if done: 
        return reward
    return reward + gamma * max_q_value(q_table, next_state)

def td_error(target, q_table, state, action):
    # TODO: return the TD error: target minus current Q(state, action)
    return target - q_table[state][action]

def q_learning_update(q_table, state, action, reward, next_state, done, alpha, gamma):
    # TODO: apply Q(s,a) += alpha * (target - Q(s,a)) in place and return the new Q value
    target = td_target(reward, gamma, q_table, next_state, done)
    error = td_error(target, q_table, state, action)
    q_table[state][action] += alpha * error
    return q_table[state][action]

def interaction_step(env, q_table, state, epsilon, alpha, gamma, rng):
    # TODO: select epsilon-greedy action, step env, apply Q-learning update, return (next_state, reward, done)
    new_action = epsilon_greedy_action(q_table, state, epsilon, env.action_space, rng)
    obs, reward, terminated, truncated , info = env.step(new_action)
    done = terminated or truncated
    q_learning_update(q_table, state, new_action, reward, obs, done, alpha, gamma)
    return (int(obs), float(reward), bool(done))

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

def train_q_learning(env, num_episodes, alpha=0.1, gamma=0.99, epsilon_start=1.0, epsilon_min=0.05, epsilon_decay=0.995, seed=0, max_steps=200):
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

def extract_greedy_policy(q_table):
    # TODO: return a 1D int64 array mapping each state to its best (argmax) action.
    policy = np.empty(shape=len(q_table), dtype=np.int64)
    N = len(q_table)
    for state in range(N):
        policy[state]=greedy_action(q_table, state)

    return policy

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

def evaluate_success_rate(env, policy, num_episodes, seed=0, max_steps=200):
    # TODO: run num_episodes greedy rollouts and return the fraction that reached the goal.
    env.reset(seed=seed)
    env.action_space.seed(seed)

    success = 0
    for episode in range(num_episodes):
        reached_goal = run_greedy_episode(env, policy, seed=seed + episode, max_steps=max_steps)
        success += reached_goal / num_episodes

    return success

"""Q-Learning on FrozenLake: train a tabular agent and evaluate its greedy policy."""
 
if __name__ == "__main__":
    np.random.seed(0)
 
    # Build a non-slippery FrozenLake for faster, more reliable learning.
    env = gym.make("FrozenLake-v1", is_slippery=False)
    env.action_space.seed(0)
 
    num_states = env.observation_space.n
    num_actions = env.action_space.n
    print(f"FrozenLake: {num_states} states, {num_actions} actions")
 
    # Train the tabular Q-learning agent.
    q_table, reward_history = train_q_learning(
        env,
        num_episodes=2000,
        alpha=0.1,
        gamma=0.99,
        epsilon_start=1.0,
        epsilon_min=0.05,
        epsilon_decay=0.995,
        seed=0,
        max_steps=200,
    )
    print(f"Q-table shape: {q_table.shape}")
    print(f"Reward history length: {len(reward_history)}")
    early_avg = float(np.mean(reward_history[:100]))
    late_avg = float(np.mean(reward_history[-100:]))
    print(f"Mean reward first 100 episodes: {early_avg:.3f}")
    print(f"Mean reward last 100 episodes:  {late_avg:.3f}")
 
    # Extract greedy policy and inspect a couple of Q-values.
    policy = extract_greedy_policy(q_table)
    print(f"Greedy policy (first 8 states): {policy[:8].tolist()}")
    print(f"Greedy action at state 0: {greedy_action(q_table, 0)}")
    print(f"Max Q-value at state 0: {max_q_value(q_table, 0):.4f}")
 
    # Run one greedy episode and report success.
    reached_goal = run_greedy_episode(env, policy, seed=0, max_steps=200)
    print(f"Single greedy episode reached goal: {bool(reached_goal)}")
 
    # Evaluate success rate over many greedy episodes.
    success_rate = evaluate_success_rate(env, policy, num_episodes=100, seed=0, max_steps=200)
    print(f"Greedy success rate over 100 episodes: {success_rate:.2f}")
 
    env.close()
