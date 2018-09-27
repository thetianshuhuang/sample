
"""Monte Carlo Simulation Framework

Examples
--------
>>> from sample import HaltonSequence, MonteCarlo
>>> v = lambda point: point[0]**2 + point[1]**2 < 1
>>> pi = MonteCarlo(v, 1000000, sample=HaltonSequence, dim=2).mean * 4
>>> pi
3.1415968
"""

import warnings
import time
from .sample import SimpleRandomSample


class SamplePoint:
    """Sample point storage class

    Attributes
    ----------
    point : arbitrary type
        Provided point
    value : arbitrary type
        Computed value using value_function

    Parameters
    ----------
    point : arbitrary type
        Input data to store
    value_function: point -> value
        Function that computes a value from an input sample point
    """
    def __init__(self, point, value_function):
        self.point = point
        self.value = value_function(point)


class MonteCarlo:
    """Monte Carlo simulation class

    Attributes
    ----------
    n : int
        Number of samples taken
    values : SamplePoint[]
        List of ``SamplePoint`` objects corresponding to each sample and sample
        result
    mean : float
        Mean return value if the return type of value_function is float;
        otherwise, is set as ``None``

    Parameters
    ----------
    value_function : function(point) -> value
        Value function to run on all samples; should return float, int, or
        bool (boolean values are mapped to 1 if True and 0 if False)
    n : int
        Number
    kwargs : dict
        All keyword args are passed onto the sample function

    Keyword Args
    ------------
    sample : iterator
        Generator for sample points; should use Python's iterator syntax.
        For an example, see BaseSampler. Defaults to SimpleRandomSample.
    """

    def __init__(
            self, value_function, n,
            sample=SimpleRandomSample, **kwargs):

        start_time = time.time()

        # Check for integer n
        if type(n) != int:
            warning = (
                "The number of samples {samples} is not an integer, and has "
                "been rounded down to an integer.").format(samples=n)
            warnings.warn(warning)
            n = int(n)
        self.n = n

        if "store" in kwargs and kwargs["store"]:

            # Get values and store in SamplePoint classes
            self.values = [
                SamplePoint(point, value_function)
                for point in sample(n, **kwargs)]

            # Compute mean
            try:
                self.mean = sum(
                    float(point.value) for point in self.values) * 1. / self.n
            # Catch exceptions
            except Exception as e:
                warnings.warn(
                    "Exception occured while trying to convert return value" +
                    "to float: " + str(e))

        else:
            total = 0
            for point in sample(n, **kwargs):
                total += value_function(point)
            self.mean = total * 1. / n

        self.time = time.time() - start_time
