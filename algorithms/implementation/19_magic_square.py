#!/bin/python3

import os
import unittest

pre_calculated_matrix = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]


# i.e, input is
# 4 9 2
# 3 5 7
# 8 1 5
# so just calculate how much is required to make
# [4, 9, 2] --> [8, 1, 6], then [6, 1, 8], ...
# the "cost" is sum([4, 9, 2] - sum([x]), in absolute values
def forming_magic_square(input_matrix):
    totals = []
    for magic in pre_calculated_matrix:
        partial_sum = 0
        for x, y in zip(input_matrix, magic):
            partial_sum += abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])
        totals.append(partial_sum)

    return min(totals)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = forming_magic_square(s)

    fptr.write(str(result) + '\n')
    fptr.close()


class TestSolution(unittest.TestCase):
    def test_function(self):
        self.assertEquals(forming_magic_square([[4, 9, 2],
                                               [3, 5, 7],
                                               [8, 1, 5]]), 1)
