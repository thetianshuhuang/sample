
from sample import HaltonSequence, ThreadedMonteCarlo


def in_circle(x):
    return x[0]**2 + x[1]**2 < 1


def compute_pi(n):
    mc = ThreadedMonteCarlo(in_circle, n, sample=HaltonSequence, dim=2)
    print(
        (
            "Pi={mean} computed using {samples} " +
            "elements of the Halton Sequence in {time} seconds")
        .format(samples=n, time=mc.time, mean=mc.mean * 4))


if __name__ == "__main__":
    compute_pi(10000000)
