# Sample

A collection of low-discrepancy sampling routines

<img src="https://github.com/thetianshuhuang/sample/blob/master/voronoi.png">

## Usage

The ```sample``` module provides several low-discrepancy sampling iterators. All iterators are initialized with the number of desired samples, and an optional dimension argument:

```python
>>> from sample import HaltonSequence
>>> [i for i in HaltonSequence(5, dim=2)]
[[0.0, 0.0], [0.5, 0.3333333333333333], [0.25, 0.6666666666666666], [0.75, 0.1111111111111111], [0.125, 0.4444444444444444]]
```

-```HaltonSequence```: [Halton Sequence](https://en.wikipedia.org/wiki/Halton_sequence) iterator
-```HammersleySequence```: [Hammersley Set](https://en.wikipedia.org/wiki/Low-discrepancy_sequence#Hammersley_set) iterator
-```BaseSampler```: extend this by overriding the ```BaseSampler.sample``` method to easily create new random sampling iterators. See ```SimpleRandomSample``` for an example of how to use this class.
