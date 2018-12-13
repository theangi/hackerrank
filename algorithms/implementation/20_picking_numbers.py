#!/bin/python3

import os
import unittest
from collections import Counter
from itertools import combinations


def picking_numbers(a):
    if not a:
        return 0

    counter = Counter(a)
    distinct_values = list(counter)

    if len(distinct_values) == 1:
        return len(a)

    pairs = [x for x in combinations(distinct_values, 2) if abs(x[0] - x[1]) <= 1]
    if not pairs:
        return 1

    pairs_max = max([counter[x] + counter[y] for x, y in pairs])
    freq_most_common = counter.most_common()[0][1]
    return pairs_max if pairs_max > freq_most_common else freq_most_common


def short_but_inefficient_function(a):
    return max(a.count(x) + a.count(x + 1) for x in set(a)) if a else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = picking_numbers(a)

    fptr.write(str(result) + '\n')
    fptr.close()


class TestSolution(unittest.TestCase):
    def test_function(self):
        self.assertEquals(picking_numbers([4, 6, 5, 3, 3, 1]), 3)
        self.assertEquals(picking_numbers([1, 2, 2, 3, 1, 2]), 5)
        self.assertEquals(picking_numbers([]), 0)
        self.assertEquals(picking_numbers([1]), 1)
        self.assertEquals(picking_numbers([1, 5, 8]), 1)
        self.assertEquals(picking_numbers([1, 1, 1]), 3)
        self.assertEquals(picking_numbers(
            [4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5,
             97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5,
             97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97,
             5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]), 50)

    def test_short_function(self):
        self.assertEquals(short_but_inefficient_function([4, 6, 5, 3, 3, 1]), 3)
        self.assertEquals(short_but_inefficient_function([1, 2, 2, 3, 1, 2]), 5)
        self.assertEquals(short_but_inefficient_function([]), 0)
        self.assertEquals(short_but_inefficient_function([1]), 1)
        self.assertEquals(short_but_inefficient_function([1, 5, 8]), 1)
        self.assertEquals(short_but_inefficient_function([1, 1, 1]), 3)
        self.assertEquals(short_but_inefficient_function(
            [4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5,
             97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5,
             97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97,
             5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]), 50)
