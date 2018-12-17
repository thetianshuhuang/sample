
import matplotlib.pyplot as plt
from sample import HaltonSequence, HammersleySequence
from scipy.spatial import Voronoi, voronoi_plot_2d


def visualize_points(points):
    """Visualize a list of 2-dimensional points.

    Paramters
    ---------
    points : int[][]
        List of 2d coordinates
    """

    x, y = list(zip(*points))
    plt.scatter(x, y, s=1)
    plt.show()


def star_discrepancy(points, N):
    """Estimate the star discrepancy of a list of points.

    Parameters
    ----------
    points : int[][]
        List of points in [0,1]x[0,1]
    N : int
        Number of rectangles to draw (each i/N x j/N)

    Returns
    -------
    float
        Estimated star discrepancy.
    """

    max_discrepancy = 0
    for i in range(N):
        for j in range(N):

            in_rect = 0
            for x in points:
                if x[0] < i * 1. / N and x[1] < j * 1. / N:
                    in_rect += 1

            max_discrepancy = max(
                max_discrepancy,
                in_rect * 1. / len(points) - (i * j * 1.) / (N**2))

    return max_discrepancy


if __name__ == "__main__":

    halton = [i for i in HaltonSequence(500, dim=2)]
    hammersley = [i for i in HammersleySequence(500, dim=1)]

    N = 100

    print(
        "Halton sequence star discrepancy with N={length}: {value}"
        .format(length=N, value=star_discrepancy(halton, N)))
    visualize_points(halton)
    vor = Voronoi(halton)
    voronoi_plot_2d(vor)
    plt.show()

    print(
        "Hammersley sequence star discrepancy with N={length}: {value}"
        .format(length=N, value=star_discrepancy(hammersley, N)))
    visualize_points(hammersley)
    vor = Voronoi(hammersley)
    voronoi_plot_2d(vor)
    plt.show()
