
import numpy as np
from matplotlib import pyplot as plt
from sample import BoxMuller


def compare_to_normal(points, num_bins):
    """Compare a list of points in R to the normal distribution
    centered at 0.

    Parameters
    ----------
    points : float[]
        List of points
    num_bins : int
        Number of bins to draw
    """

    figure, a = plt.subplots()
    n, bins, patches = a.hist(points, num_bins, density=1)
    normal = (
        (1 / (np.sqrt(2 * np.pi) * 1)) * np.exp(-0.5 * (1. * bins) ** 2))
    a.plot(bins, normal, '--')
    plt.show()


def compare_box_muller(n, bins=50):
    """Compare Box-Muller samples to the bivariate normal.

    Parameters
    ----------
    n : int
        Number of trials
    bins : int
        Number of bins to draw
    """

    samples = [i for i in BoxMuller(n, dim=2)]
    x, y = list(zip(*samples))

    plt.scatter(x, y, s=1)
    plt.show()

    # X axis comparison
    compare_to_normal(x, bins)

    # Y axis comparison
    compare_to_normal(y, bins)


if __name__ == "__main__":
    compare_box_muller(100, bins=20)
    compare_box_muller(10000, bins=100)
