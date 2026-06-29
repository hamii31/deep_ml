import numpy as np

def extract_optimal_policy(Q: np.ndarray) -> dict:
    """
    Extract the optimal policy, state-value function, and advantage
    function from a Q-value table.
    
    Args:
        Q: Q-value table of shape (num_states, num_actions)
    
    Returns:
        Dictionary with keys:
        - 'optimal_actions': list of int (optimal action per state)
        - 'state_values': list of float (V*(s) per state)
        - 'advantages': nested list of float (A(s,a) for all pairs)
    """
    optimal_actions = []
    state_values = []
    advantages = []
  
    for state in Q:
        advantage = []
        v_s = np.max(state)
        for i in state:
            advantage.append(round(float(i - v_s), 2))
        
        state_values.append(float(v_s))
        optimal_actions.append(int(np.where(state == v_s)[0][0])) # first occurence of v_s
        advantages.append(advantage)

    return {
        'optimal_actions':optimal_actions,
        'state_values':state_values,
        'advantages':advantages
        }

Q = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [9.0, 8.0, 7.0]])
result = extract_optimal_policy(Q)
print(result)

Q = np.array([[0.5, 0.3, 0.8, 0.1], [0.2, 0.7, 0.4, 0.6], [0.9, 0.1, 0.3, 0.5], [0.4, 0.4, 0.4, 0.4]])
result = extract_optimal_policy(Q)
print(result)
