
import math
from sample import MonteCarlo


def in_circle(x):
    return x[0]**2 + x[1]**2 < 1


def chernoff_verification(epsilon, delta, n):
    """Verify the chernoff bound.

    Parameters
    ----------
    epsilon : float
        Maximum error
    delta : float
        Expectation bound (is in the epsilon bound 1-delta of the time)
    n : int
        Number of trials
    """

    bound = 12. / (math.pi * epsilon**2) * math.log(2. / delta)

    print(
        (
            "Chernoff Inequality bound for epsilon = {epsilon}" +
            " and delta = {delta}: n = {bound}")
        .format(epsilon=epsilon, delta=delta, bound=int(bound))
    )

    trials = [
        MonteCarlo(in_circle, int(bound), dim=2).mean * 4 for i in range(n)]

    in_range = 0
    for i in trials:
        if (abs(math.pi - i)) / math.pi < delta * 0.1:
            in_range += 1

    print("Trials tested: " + str(n))
    print("Proportion in range: " + str(in_range * 1. / n))


if __name__ == "__main__":
    chernoff_verification(0.1, 0.1, 1000)
