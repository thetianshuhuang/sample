
"""Python sampling framework"""

import random


class BaseSampler:
    """Base sampler iterator class

    Extend this class to use iterator behavior with a random sampler.

    Attributes
    ----------
    i : int
        Current index
    kwargs : dict
        Dictionary of keyword args passed to init

    Parameters
    ----------
    n : int
        Maximum number of iterations to run
    kwargs : dict
        Keyword args passed on to sample.
    """

    def __init__(self, n, **kwargs):
        self.i = 0
        self.n = n
        self.kwargs = kwargs

    def __iter__(self):
        """__iter__ function called by python to get the iterator object"""
        return self

    def __next__(self):
        """next function called by python to get the next value"""
        if self.i < self.n:
            self.i += 1
            return self.sample(self.i - 1, **self.kwargs)
        else:
            raise StopIteration()

    def next(self):
        """Non-dunder next method for python2 compatibility"""
        return self.__next__()

    def sample(self, idx, **kwargs):
        """Placeholder function

        This method must be overwritten by classes extending BaseSampler.

        Parameters
        ----------
        idx : int
            Current index
        kwargs : dict
            Dictionary of values passed to the iterator constructor

        Raises
        ------
        Exception
            This method should never be called.
        """
        raise Exception(
            "Attempted to call base sampler class without" +
            "overriding BaseSampler.next")
        return None


class SimpleRandomSample(BaseSampler):
    """Simple random sampler

    Iterator that returns numbers between 0 and 1 with dimension dim using
    Python's random.random module.
    """

    def sample(self, idx, **kwargs):
        """Simple random sample iterator

        Keyword Args
        ------------
        dim : int
            Number of dimensions to return
        """

        if "dim" in kwargs:
            d = kwargs["dim"]
        else:
            d = 1

        return [random.random() for i in range(d)]
