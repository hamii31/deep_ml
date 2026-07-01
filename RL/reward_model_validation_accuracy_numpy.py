import numpy as np

def reward_model_validation(
    chosen_scores: np.ndarray,
    rejected_scores: np.ndarray,
    margin_thresholds: list[float]
) -> dict:
    """
    Compute validation metrics for a reward model on held-out preference pairs.

    Args:
        chosen_scores: 1D array of reward scores for preferred responses.
        rejected_scores: 1D array of reward scores for rejected responses.
        margin_thresholds: List of thresholds for margin-based accuracy.

    Returns:
        Dictionary with 'accuracy', 'mean_margin', 'concordance', 'margin_accuracy'.
    """
    margins = chosen_scores - rejected_scores

    wins = 0
    ties = 0
    N = len(margins)
    for i in range(N):
        if margins[i] > 0: wins+=1
        if margins[i] == 0: ties+=1

    accuracy = round(wins / N,4)

    mean_margin = float(np.mean(margins))

    concordance = round((wins + 0.5 * ties) / N,4)

    margin_accuracy = {}
    for thresholds in enumerate(margin_thresholds):
        win_pairs = 0
        threshold = thresholds[1]
        for i in range(N):
            if margins[i] >= threshold: win_pairs+=1

        margin_accuracy[threshold] = round(win_pairs / N,4)

    return {
        'accuracy': accuracy, 
        'mean_margin': mean_margin, 
        'concordance': concordance, 
        'margin_accuracy': margin_accuracy
        }
