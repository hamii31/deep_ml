def should_explore(epsilon, rng):
    """Return True with probability epsilon using the provided numpy Generator."""
    # TODO: draw a uniform sample from rng and compare it to epsilon
    return epsilon > rng.random()
