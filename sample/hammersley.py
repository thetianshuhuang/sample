
"""Hammersley sequence iterator"""


from .sample import BaseSampler
from .halton import halton_sequence


class HammersleySequence(BaseSampler):
    """N-dimensional Hammersley sequence iterator"""

    def sample(self, idx, **kwargs):
        """Hammersley sequence iterator

        Keyword Arguments
        -----------------
        dim : int
            Number of extra dimensions to use for a total of dim + 1 dimensions
        base : int[]
            List of integers to use as the base. Should be relatively prime. If
            base is not provided, then the first ``dim`` primes will be used.
        skip : int
            Number of samples to skip at the beginning

        Returns
        -------
        float[d]
            d dimensional vector in (0,1)^d.
        """

        return [float(idx) / self.n] + halton_sequence(idx, **kwargs)
