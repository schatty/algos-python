"""
Given the stream of input integers provide uniform sampler of size k.
"""

from itertools import islice
from random import randint

def sample_uniform(stream, k):
    res = list(islice(stream, k))
    n_seen = k

    for x in stream:
        r = randint(0, n_seen - 1)
        if r < k:
            res[r] = x
        n_seen += 1

    return res


s = [1, 0, 2, 8, 3, 2, 1, 4, 6, 7]
print(sample_uniform(s, k=4))
