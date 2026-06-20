import numpy as np

def discounted_return(rewards, gamma):
    """
    Compute the total discounted return for a sequence of rewards.
    Args:
        rewards (list or np.ndarray): List or array of rewards [r_0, r_1, ..., r_T-1]
        gamma (float): Discount factor (0 < gamma <= 1)
    Returns:
        float: Total discounted return
    """
    # Your code here
    G_t = rewards[0]
    rewards = rewards[1:]
    n = len(rewards)
    k = 1

    for i in range(n):
        G_t += rewards[i] * gamma**k
        k+=1

    return G_t
