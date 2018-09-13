
"""Hammersley sequence iterator"""

import math
from .sample import BaseSampler


class HammersleySequence(BaseSampler):
    """N-dimensional Hammersley sequence iterator"""

    def reverse_bin(self, i, power):
        """Helper method to reverse a binary integer

        Parameters
        ----------
        i : int
            Int to reverse

        Returns
        -------
        int
            i, bitwise reversed
        """

        reverse = 0
        while i > 0:
            reverse *= 2
            reverse += i % 2
            i = math.floor(i / 2)
            power -= 1
        return reverse * (2**power)

    def sample(self, idx, **kwargs):
        """Hammersley sequence iterator"""

        power = math.ceil(math.log(self.n, 2))

        return [
            float(idx) / self.n,
            float(self.reverse_bin(idx, power)) / self.n
        ]
