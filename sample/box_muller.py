
"""Box-Muller sampling"""


import random
import math
from .sample import BaseSampler


class BoxMuller(BaseSampler):
    """Box-Muller sampling iterator"""

    def sample(self, idx, **kwargs):
        """Box Muller sample function

        Returns
        -------
        float[2]
            Two element array corresponding to the resulting [x,y]
            cooardinates in R^2.
        """

        x = [random.random(), random.random()]

        return [
            math.sqrt(-2 * math.log(x[0])) * math.cos(2 * math.pi * x[1]),
            math.sqrt(-2 * math.log(x[0])) * math.sin(2 * math.pi * x[1]),
        ]
