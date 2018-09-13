
"""Monte Carlo Simulation Framework"""


class MonteCarlo:
    """
    """

    def __init__(self, sample, verify, **kwargs):
        self.sample = sample
        self.verify = verify
        self.kwargs = kwargs

        self.samples = None
        self.n = None
        self.count = None
        self.result = None

    def run(self, n):

        self.samples = [
            {"s": point, "val": self.verify(point)}
            for point in self.sample(n)
        ]
        self.count = 0
        self.n = n
        for r in self.results:
            if r["val"]:
                self.count += 1
        self.result = float(self.count) / self.n
