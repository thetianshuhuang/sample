
import sys
from sample import HaltonSequence, MonteCarlo


def in_circle(x):
    return x[0]**2 + x[1]**2 < 1


def compute_pi(n):
    mc = MonteCarlo(in_circle, n, sample=HaltonSequence, dim=2)
    print(
        (
            "Pi={mean} computed using {samples} " +
            "elements of the Halton Sequence in {time} seconds")
        .format(samples=n, time=mc.time, mean=mc.mean * 4))


if __name__ == "__main__":

    try:
        compute_pi(int(sys.argv[1]))
    except Exception as e:
        print("Invalid input:" + str(e))
