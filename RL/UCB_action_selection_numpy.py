import numpy as np

def ucb_action(counts, values, t, c):
    """
    Choose an action using the UCB1 formula.
    Args:
      counts (np.ndarray): Number of times each action has been chosen
      values (np.ndarray): Average reward of each action
      t (int): Current timestep (starts from 1)
      c (float): Exploration coefficient
    Returns:
      int: Index of action to select
    """
    # TODO: Implement the UCB action selection
    USB = [values[i] + np.sqrt((2 * np.log(t) / counts[i])) for i in range(len(values))]
    return USB.index(max(USB))

counts = np.array([1, 1, 1, 1])  # Each action tried once
values = np.array([1.0, 2.0, 1.5, 0.5])
t = 4
c = 2.0
print(ucb_action(counts, values, t, c))
