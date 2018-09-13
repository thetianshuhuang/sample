
"""Halton sequence iterator"""


import math
from .sample import BaseSampler


def halton_sample_1d(base, idx):
    """Get one dimensional halton sequence

    Parameters
    ----------
    base : int
    base : int[]
        List of integers to use as the b
        Halton sequence base
    idx : int
        Current sequence index

    Returns
    -------
    float
        Result, between 0 and 1.
    """

    # Initialize as floating point numbers
    current_frac = 1.
    result = 0.

    while idx > 0:
        current_frac = current_frac / base
        result += current_frac * (idx % base)
        idx = math.floor(idx / base)

    return result


def halton_sequence(idx, **kwargs):
    """Get the nth element of a halton sequence.

    Parameters
    ----------
    idx : int
        Index of the element to get

    Keyword Arguments
    -----------------
    dim : int
        Number of dimensions to use
    base : int[]
        List of integers to use as the base. Should be relatively prime. If
        base is not provided, then the first ``dim`` primes will be used.
    skip : int
        Number of samples to skip at the beginning
    """

    d = 1 if "dim" not in kwargs else kwargs["dim"]
    idx += 0 if "skip" not in kwargs else kwargs["skip"]

    # We assume that the user will supply coprime integers if this class
    # is used beyond a simple example.
    if d <= 5 and "base" not in kwargs:
        base = [2, 3, 6, 7, 11][:(d)]
    elif d > 5 and "base" not in kwargs:
        raise Exception("Coprime bases must be supplied for d>=5.")
    else:
        base = kwargs["base"]

    # Build return array
    return [halton_sample_1d(b, idx) for b in base]


class HaltonSequence(BaseSampler):
    """N-dimensional Halton sequence iterator"""

    def sample(self, idx, **kwargs):
        """Halton sequence iterator

        Keyword Arguments
        -----------------
        dim : int
            Number of dimensions to use
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

        return halton_sequence(idx, **kwargs)
